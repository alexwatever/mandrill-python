import mandrill
import csv
import logging

# set data file
data = 'list.csv'

# setup logging
log = 'send.log'
logging.basicConfig(filename=log, format='%(asctime)s %(message)s', level=logging.INFO)

# set api key
API_KEY = ''

# set variables
template = 'website-password-change'


def send_mail(template_name, key, data):
    # load mandrill
    mandrill_client = mandrill.Mandrill(key)

    # start counter
    num = 1

    # load email list
    with open(data, "r") as f:
        reader = csv.reader(f, delimiter=",")

        # loop through recipients
        for row in reader:

            # create message shell
            message = {
                'to': [],
                'global_merge_vars': []
            }

            # add recipient email
            message['to'].append({'email': row[0]})

            # add recipient name
            message['global_merge_vars'].append(
                {'name': 'name', 'content': row[1]}
            )

            # send
            mandrill_client.messages.send_template(template_name, [], message)

            # log results
            logging.info(
                '"Row: %d","Email: %s","Name: %s"' % (num, row[0], row[1])
            )

            # print confirmation to console            
            print('Sent %d to %s[%s]') % (num, row[1], row[0])
            num += 1


# call function to send mail
send_mail(template, API_KEY, data)
print('All done')

