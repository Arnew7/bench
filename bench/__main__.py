import asyncio
import sys
from .cli import parse_args, load_hosts
from .runner import bench_all
from .reporter import format_report

async def main(argv):
    try:
        args = parse_args(argv)
        if args.count <= 0:
            raise ValueError("--count должен быть > 0")
        hosts = load_hosts(args)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 2

    reports = await bench_all(hosts, args.count)
    report = format_report(reports)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report + "\n")
    else:
        print(report)
    return 0

if __name__ == "__main__":
    sys.exit(asyncio.run(main(sys.argv[1:])))
