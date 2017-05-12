from nupic.swarming import permutations_runner
from swarm_description import SWARM_DESCRIPTION
import os
def swarm(inputFile):
    swarmWorkDir = os.path.abspath("swarm")
    if not os.path.exists(swarmWorkDir):
        os.mkdir(swarmWorkDir)
    permutations_runner.runWithConfig(
        SWARM_DESCRIPTION,
        {
            "maxWorkers": 4,
            "overwrite": True
        },
        outputLabel ="rec center",
        outDir =swarmWorkDir,
        permWorkDir =swarmWorkDir
    )
if __name__ == '__main__':
    swarm('rec-center-hourly.csv')