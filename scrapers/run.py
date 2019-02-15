from .common import workbook, run_common

from .gs import run_gs
from .cj import run_cj
from .hyundai import run_hyundai
from .ns import run_ns

def run():
    run_common()
    run_gs()
    run_cj()
    run_hyundai()
    run_ns()
    workbook.close()

if __name__ == '__main__':
	  run()
