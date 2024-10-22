import os
import logging
from threading import Thread

__version__ = '1.3.6'

# NOTE: DISABLE Version Check !!!!! The thread may result in deadloack when the program is quitting
# try:
#     os.environ['OUTDATED_IGNORE'] = '1'
#     from outdated import check_outdated  # noqa
# except ImportError:
#     check_outdated = None


# def check():
#     try:
#         is_outdated, latest = check_outdated('ogb', __version__)
#         if is_outdated:
#             logging.warning(
#                 f'The OGB package is out of date. Your version is '
#                 f'{__version__}, while the latest version is {latest}.')
#     except Exception:
#         pass


# if check_outdated is not None:
#     thread = Thread(target=check)
#     thread.start()
