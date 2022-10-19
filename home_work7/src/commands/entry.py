from commands.help_command import help_command
from commands.show_phone_book_command import show_phone_book_command
from commands.start_command import start_command
from commands.convert_to_command import convert_to_command

commands = {
    'start': {
        'command_handler': start_command,
        'description': 'Отправляет приветственное сообщение'
    },
    'convert_to': {
        'command_handler': convert_to_command,
        'description': "Преобразование формата хранения данных в заданный formatId. Пример использования: '/convert_to {formatId}'"
    },
    'help': {
        'command_handler': help_command,
        'description': 'Отображает список доступных команд'
    },
    'show': {
        'command_handler': show_phone_book_command, 
        'description': 'Отображает данные из телефонного справочника'
    }
}
