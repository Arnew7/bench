import argparse
import re
from typing import List

HOST_REGEX = re.compile(r"^https://[A-Za-z0-9.-]+(?::\d+)?(?:/.*)?$")

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Тестовое задание "Асинхронный HTTP-бенчмарк"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-H", "--hosts", help="Список адресов через запятую")
    group.add_argument("-F", "--file", help="Файл со списком адресов")
    parser.add_argument("-C", "--count", type=int, default=1, help="Количество запросов")
    parser.add_argument("-O", "--output", help="Файл для сохранения отчёта")
    return parser.parse_args(argv)

def load_hosts(args: argparse.Namespace) -> List[str]:
    hosts: List[str] = []
    if args.hosts:
        hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]
    elif args.file:
        with open(args.file, encoding="utf-8") as f:
            hosts = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not hosts:
        raise ValueError("Список хостов пуст")

    invalid = [h for h in hosts if not HOST_REGEX.match(h)]
    if invalid:
        raise ValueError("Неверные адреса: " + ", ".join(invalid))

    return hosts
