from pathlib import Path
from dataclasses import dataclass
from typing import Type, Optional, Any, List, Tuple
import math


@dataclass
class CompetitionParameters:
    """Class defining model parameters"""

    # Reward percentage
    reward_percentage: float
    # Competition id
    competition_id: str


# ---------------------------------
# Project Constants.
# ---------------------------------

# The uid for this subnet.
SUBNET_UID = 164
# The start block of this subnet
SUBNET_START_BLOCK = 2635801
# The root directory of this project.
ROOT_DIR = Path(__file__).parent.parent
# Schedule of model architectures
COMPETITION_SCHEDULE: List[CompetitionParameters] = [
    CompetitionParameters(
        reward_percentage=1.0,
        competition_id="midjourney:text2img",
    ),CompetitionParameters(
        reward_percentage=0.0,
        competition_id="midjourney:img2img",
    ),CompetitionParameters(
        reward_percentage=0.0,
        competition_id="midjourney:faceswap",
    ),
]
ORIGINAL_COMPETITION_ID = "midjourney:text2img"

assert math.isclose(sum(x.reward_percentage for x in COMPETITION_SCHEDULE), 1.0)