from datetime import datetime
import os


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    quit()


class ErrorLog:
    def write_to_log(self, log_name, data):
        with open(log_name, "a") as log:
            log.write(data)

    def write_to_error_log(self, data):
        self.write_to_log("Logs/error_log.txt", data)

    def write_to_inst_log(self, data):
        self.write_to_log("Logs/installation_log.txt", data)


def handle_error(err, is_error=True):
    error_log = ErrorLog()
    now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    if is_error:
        message = "Time {} - Error {}: {} with args {}\r\n".format(now, type(err), err, err.args)
    else:
        message = "Time {} - Error {}\r\n".format(now, err)
    error_log.write_to_error_log(message)


def handle_inst_act(action):
    error_log = ErrorLog()
    message = "Time {} - {}\r\n".format(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"), action)
    error_log.write_to_inst_log(message)


def txt_file_to_dict(file_obj):
    dict_ = {}
    file_strings = file_obj.read().decode("utf-8").split("\n")
    for string in file_strings:
        if " = " in string:
            key, value = tuple(string.split(" = "))
            dict_[key.strip()] = value.strip()
    return dict_


def is_admin():
    import ctypes
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
