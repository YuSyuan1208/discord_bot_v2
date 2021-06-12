# =========================================================================
# Addons
# =========================================================================
import logging
from modules import loading

_logger = logging.getLogger(__name__)

loading.AddonsModuleImport()
_logger.debug(loading.addons_list)
