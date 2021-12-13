# ffxiv login server: 204.2.229.9
import pyshark
import winsound
import time
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

# define human readable names for filters
FFXIV_LOGIN_SERVER = "204.2.229.9"
from_login_server = f"ip.src=={FFXIV_LOGIN_SERVER}"
initiates_closing_connection = "tcp.connection.fin_active"


def sniff_continuously(interface, display_filter):
    logger.info(f"Listening on interface: {interface}")
    logger.info(f"Using display filter: {display_filter}")
    capture = pyshark.LiveCapture(
        interface=interface,
        display_filter=display_filter
    )

    for packet in capture.sniff_continuously():
        # Skip is packet is too small for reconnect
        logger.info("Packet arrived, playing audio")
        logger.debug(packet)
        for i in range(0, 5):
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            time.sleep(1)


if __name__ == '__main__':
    sniff_continuously(
        interface="Ethernet",
        display_filter=f"({from_login_server})&&({initiates_closing_connection})"
        # display_filter="",
    )
