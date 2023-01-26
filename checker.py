import argparse

from subprocess import PIPE, Popen, run, DEVNULL
from threading import Thread
from time import sleep
from samples import SAMPLES
from queue import Queue, Empty
from pathlib import Path
from json import dump, load
from os.path import exists

from rich import print
from rich.spinner import Spinner
from rich.align import Align
from rich.live import Live
from rich.layout import Layout, Panel
from rich.table import Table, Column
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

stdout_q = Queue()
proc: Popen = None
errors = []
stdout_reader: Thread = None
err_reader: Thread = None


def enqueue_output(out):
    for line in iter(out.readline, ""):
        stdout_q.put_nowait(line)
    out.close()


def err_recorder(err):
    for line in iter(err.readline, ""):
        errors.append(line)
    err.close()


def exec_solution(solution: Path):
    global proc, err_reader, stdout_reader
    proc = Popen(
        ["coverage", "run", "-p", solution],
        stdout=PIPE,
        stderr=PIPE,
        stdin=PIPE,
        encoding="utf-8",
    )
    sleep(0.2)
    if proc.poll() is not None:
        return False
    stdout_reader = Thread(target=enqueue_output, args=(proc.stdout,))
    err_reader = Thread(target=err_recorder, args=(proc.stderr,))
    stdout_reader.daemon = True
    err_reader.daemon = True
    stdout_reader.start()
    err_reader.start()
    return True


def read_line(timeout=10) -> str:
    try:
        line = stdout_q.get(True, timeout)
    except Empty:
        raise TimeoutError("")
    return line.strip()


def write_line(*line: str, end="\n", sep=" ") -> bool:
    if proc.poll() is not None:
        return False
    line = sep.join(line) + end
    proc.stdin.write(line)
    proc.stdin.flush()
    return True


def current_solution_table(test_results, outputs, name):
    table = Table("No.", "Testcase name", Column("Output", width=10), " ", title=name)
    for i, (res, output) in enumerate(zip(test_results, outputs)):
        output = str(output)
        output = output[:7] + "[/]..." if len(output) > 10 else output
        if res is Ellipsis:
            table.add_row(
                str(i + 1), SAMPLES[i]["name"], Spinner("arc"), Spinner("arc")
            )
        elif res is None:
            table.add_row(
                str(i + 1),
                SAMPLES[i]["name"],
                "[red]" + output,
                "⚠",
            )
        elif res:
            table.add_row(
                str(i + 1),
                SAMPLES[i]["name"],
                "[green]" + output,
                "[green]✔",
            )
        else:
            table.add_row(
                str(i + 1),
                SAMPLES[i]["name"],
                "[red]" + output,
                "[red]x",
            )
    return table


def summary_table(total_test_result):
    table = Table("Student name", "Score", "Covered", "L-Count")
    for name, res in total_test_result.items():
        if "pending" in res:
            table.add_row(name, Spinner("arc"), Spinner("arc"), Spinner("arc"))
        else:
            table.add_row(
                name,
                (
                    "[green]"
                    if res["score"] >= 70
                    else "[yellow]"
                    if res["score"] >= 20
                    else "[red]"
                )
                + f"{res['score']:3.1f}%",
                f"{res['coverage_report']['summary']['percent_covered']:3.2f}%",
                str(res["coverage_report"]["summary"]["num_statements"]),
            )
    return table


def update_current_solution(layout, test_results, outputs, name):
    layout.update(
        Panel(
            Align(
                current_solution_table(test_results, outputs, name),
                "center",
                vertical="middle",
            ),
            title="Current solution",
            expand=True,
        )
    )


def update_summary(layout, total_test_result):
    layout.update(
        Panel(
            Align(summary_table(total_test_result), "center", vertical="middle"),
            title="Summary",
            expand=True,
        )
    )


def report(tests_results: dict):
    final_table = Table(
        "Student name", "Score", "Fails", "Covered", "L-Count", "Useless Lines"
    )
    for name, res in tests_results.items():
        final_table.add_row(
            name,
            (
                "[green]"
                if res["score"] >= 70
                else "[yellow]"
                if res["score"] >= 20
                else "[red]"
            )
            + f"{res['score']:3.3f}%",
            ", ".join(
                [
                    "[red]" + str(i) + "[/]"
                    for i, r in enumerate(res["test_results"], 1)
                    if not r
                ]
            ),
            f"{res['coverage_report']['summary']['percent_covered']:3.3f}%",
            str(res["coverage_report"]["summary"]["num_statements"]),
            ", ".join(
                map(
                    lambda x: "[yellow]" + str(x) + "[/]",
                    res["coverage_report"]["missing_lines"],
                )
            ),
        )
    print(Panel(Align(final_table, "center"), title="Final result", expand=True))


def report_single(tests_results: dict):
    name, result = next(iter(tests_results.items()))
    table = Table(show_lines=True, show_header=False)
    table.add_row(
        "Score",
        (
            "[green]"
            if result["score"] >= 70
            else "[yellow]"
            if result["score"] >= 20
            else "[red]"
        )
        + f"{result['score']:3.3f}%",
    )
    table.add_row(
        "Coverage", f"{result['coverage_report']['summary']['percent_covered']:3.3f}%"
    )
    table.add_row(
        "Lines count", str(result["coverage_report"]["summary"]["num_statements"])
    )
    table.add_row(
        "Not executed lines",
        ", ".join(
            map(
                lambda x: "[yellow]" + str(x) + "[/]",
                result["coverage_report"]["missing_lines"],
            )
        ),
    )
    for i, (sample, output, res) in enumerate(
        zip(SAMPLES, result["outputs"], result["test_results"]), 1
    ):
        if res is None:
            mark = "⚠"
        elif res:
            mark = "[green]✔[/]"
        else:
            mark = "[red]x[/]"
        table.add_row(f'{i} {mark} {sample["name"]}', output)
    print(Panel(Align(table, "center"), title=name, expand=True))


def test_solutions(solution_files: list[Path]):
    show_summary = len(solution_files) > 1
    test_results = [Ellipsis] * len(SAMPLES)
    outputs = [Ellipsis] * len(SAMPLES)
    total_test_result = {}
    for file in solution_files:
        name = file.name.rstrip(".py")
        total_test_result[name] = {"pending": True}

    progress = Progress(
        "{task.description}",
        SpinnerColumn("arc", finished_text="✔"),
        BarColumn(None),
        TextColumn("[progress.percentage]{task.percentage:>3.1f}%"),
        TextColumn("{task.fields[info]}", table_column=Column(width=50)),
    )

    test_progress = progress.add_task("Test progress", total=len(SAMPLES), info="...")
    total_progress = progress.add_task(
        "Overall progress",
        info="...",
        total=len(solution_files) * (len(SAMPLES) + 1),
    )

    layout = Layout()
    layout.split_column(
        Layout(name="upper", size=8),
        Layout(name="lower"),
    )
    if show_summary:
        layout["lower"].split_row(
            Layout(name="left"),
            Layout(name="right"),
        )
        current_solution_layout = layout["left"]
    else:
        current_solution_layout = layout["lower"]
    layout["upper"].update(
        Panel(
            progress,
            border_style="color(204)",
            padding=(2, 2),
        )
    )

    update_current_solution(current_solution_layout, test_results, outputs, name)
    if show_summary:
        update_summary(layout["right"], total_test_result)

    with Live(layout, refresh_per_second=8):
        for index, solution_file in enumerate(solution_files):
            name = solution_file.name.rstrip(".py")
            progress.update(total_progress, info=f"{name}'s solution")
            outputs = [Ellipsis] * len(SAMPLES)
            test_results = [Ellipsis] * len(SAMPLES)
            progress.reset(test_progress)
            update_current_solution(
                current_solution_layout, test_results, outputs, name
            )
            for testcase, sample in enumerate(SAMPLES):
                progress.update(
                    test_progress, info=f'Testcase {testcase+1} -> {sample["name"]}'
                )
                output, result = None, None
                if exec_solution(solution_file):
                    for inp in sample["input"]:
                        write_line(inp)
                    try:
                        output = read_line(5)
                        try:
                            proc.wait(5)
                        except TimeoutError:
                            proc.kill()
                        result = output == sample["output"]
                    except TimeoutError:
                        output = "[TIMEOUT]"
                    finally:
                        proc.kill()
                        err_reader.join()
                        stdout_reader.join()
                else:
                    output = "[EXITED]"
                outputs[testcase] = output
                test_results[testcase] = result

                # clear output buffer
                while not stdout_q.empty():
                    stdout_q.get_nowait()
                progress.advance(test_progress)
                progress.advance(total_progress)
                update_current_solution(
                    current_solution_layout, test_results, outputs, name
                )

            run("coverage combine", stdout=DEVNULL, stderr=DEVNULL)
            run("coverage json", stdout=DEVNULL, stderr=DEVNULL)
            coverage_report = load(open("coverage.json"))["files"][str(solution_file)]
            percent = test_results.count(True) / len(SAMPLES) * 100
            total_test_result[name] = {
                "score": percent,
                "test_results": test_results,
                "outputs": outputs,
                "coverage_report": coverage_report,
            }
            if show_summary:
                update_summary(layout["right"], total_test_result)
            progress.advance(total_progress)

    return total_test_result


if __name__ == "__main__":
    parser = argparse.ArgumentParser("checker.py")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-d", "--dir", nargs=1, type=Path, default=Path("./Solutions/"))
    group.add_argument(
        "-f",
        "--file",
        nargs=1,
        type=Path,
    )
    group.add_argument(
        "-r",
        "--report",
        nargs="?",
        type=argparse.FileType("r"),
        const=open("test results.json", "r") if exists("test results.json") else False,
        default=False,
    )
    group.add_argument(
        "-s",
        "--summary",
        nargs="?",
        type=argparse.FileType("r"),
        const=open("test results.json", "r") if exists("test results.json") else False,
        default=False,
    )
    args = parser.parse_args()

    if args.report:
        report(load(args.report))
    elif args.summary:
        print(
            Panel(
                Align(summary_table(load(args.summary)), "center"),
                title="Summary",
                expand=True,
            )
        )
    else:
        if not args.file:
            solution_files = list(Path("./Solutions/").glob("*.py"))
            result = test_solutions(solution_files)
            report(result)
            dump(result, open("test results.json", "w"), indent=2)
        else:
            result = test_solutions(args.file)
            report_single(result)
            if exists("test results.json"):
                test_results = load(open("test results.json", "r"))
                name, result = result.popitem()
                test_results[name] = result
                dump(test_results, open("test results.json", "w"), indent=2)
