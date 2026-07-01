import os
import importlib.util

from validator import validate_bot


def load_bots(folder="players"):

    bots = []

    for file in os.listdir(folder):

        if not file.endswith(".py"):
            continue

        path = os.path.join(folder, file)

        module_name = file[:-3]

        spec = importlib.util.spec_from_file_location(
            module_name,
            path
        )

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        bot = module.Bot()

        validate_bot(bot)

        bots.append(bot)

    return bots