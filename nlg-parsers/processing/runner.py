import asyncio
import subprocess
import threading
import multiprocessing

async def run(page_index):
    cmd = f'python script.py {page_index}'
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

# [asyncio.run(run(x)) for x in range(1,100)]


# async def function_a(): # this is being called each time when a new message arrives
#     await asyncio.gather(*(run(p_ind) for p_ind in range(1,100)))
#
# function_a()

# async def main():
#     runned_scrps=[]
#     for i in range(1,100):
#         runned_scrps.append(run(i))
#     await asyncio.gather(*runned_scrps)
#
# main()
# commands = []
# for i in range(1, 100):
#     commands.append(f'python script.py {i}')

def runcomm(ind):
   command = f'python script.py {ind}'
   subprocess.Popen(command, shell=True)

pool = multiprocessing.Pool()
pool.map(runcomm, [x for x in range(1,100)])

