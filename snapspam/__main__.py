"""The CLI for snapspam."""
import argparse
import threading
from time import sleep
import json


def main():
    """The main function to set up the CLI and run the spammers"""
    parser = argparse.ArgumentParser(
        description=
        'A CLI to spam multiple common anonymous message apps for Snapchat')

    subparsers = parser.add_subparsers(help='The app to spam',
                                       dest='target_app',
                                       required=True)

    sendit_parser = subparsers.add_parser('sendit',
                                          help='Spam a sendit sticker')
    sendit_parser.add_argument('sticker_id',
                               type=str,
                               help='The sticker ID or URL to spam')
    sendit_parser.add_argument('message', type=str, help='The message to spam')
    sendit_parser.add_argument('--msg-count',
                               type=int,
                               default=-1,
                               help='The amount of messages to send. '
                               'Set to -1 (default) to spam until stopped')
    sendit_parser.add_argument(
        '--thread-count',
        type=int,
        default=1,
        help='The amount of threads to create. Only valid for --msg-count -1. '
        'Note that the message count will NOT be divided between threads.')
    sendit_parser.add_argument(
        '--delay',
        type=int,
        default=500,
        help='Milliseconds to wait between message sends')
    sendit_parser.add_argument(
        '--sendit-delay',
        type=int,
        default=0,
        help='Minutes before the recipient gets the message '
        '(Part of sendit; not a custom feature)')

    args = parser.parse_args()

    if args.target_app == 'sendit':
        import sendit

        spammer = sendit.Sendit(args.sticker_id, args.message,
                                args.sendit_delay)

        def send():
            r = json.loads(spammer.post().content)
            if r['status'] == 'success':
                print('Sent message.')
            else:
                print('Message failed to send.')
                print(r)
            sleep(args.delay / 1000)

        if args.msg_count == -1:
            print('Sending messages until stopped.')
            print('(Stop with Ctrl + C)')
        else:
            print(f'Sending {args.msg_count} messages...')

        if args.msg_count == -1:

            def thread():
                while True:
                    send()

            for i in range(args.thread_count - 1):
                t = threading.Thread(target=thread)
                t.daemon = True
                t.start()

            # Instead of running n threads, run n - 1 and run one in the main thread
            thread()
        else:
            for _ in range(args.msg_count):
                send()


if __name__ == '__main__':
    main()
