# Abstração
# Herança - é um
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        formatted_message = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as file:
            file.write(formatted_message + '\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Top')

    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Top')
    # print(LOG_FILE)
