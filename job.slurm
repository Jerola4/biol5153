#!/usr/bin/env python3

# Define the slurm function
def run_job(partition, time, script_name):
    slurm_script = f'''#!/bin/bash

#SBATCH -J run_bash
#SBATCH --partition={partition}
#SBATCH -o errorR_%j.slurm
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jr130@uark.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time={time}

python {script_name}
'''
    with open('job.slurm', 'w') as file:
        file.write(slurm_script)

def main():
    partition = input("Enter partition: ")
    time = input("Enter time: ")
    script_name = input("Enter script name: ")

    run_job(partition, time, script_name)

if __name__ == "__main__":
    main()
 
