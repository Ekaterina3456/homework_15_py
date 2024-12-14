# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging

logging.basicConfig(filename='debug_info.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='warnings_errors.log', encoding='utf-8', level=logging.WARNING)
logger = logging.getLogger('debug_info.log')
logger1 = logging.getLogger('warnings_errors.log')

logger.debug('сообщение уровня DEBUG')
logger.info('сообщение уровня INFO')
logger1.warning('сообщение уровня WARNING')
logger1.error('сообщение уровня ERROR')
logger1.critical('сообщение уровня CRITICAL')


