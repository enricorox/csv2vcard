import csv


def csv_to_vcard(csv_filename, vcard_filename):
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(vcard_filename, 'w') as vcard_file:
            for row in csv_reader:
                try:
                    last_name = " ".join([n.capitalize() for n in row["Last Name"].split()])
                except:
                    last_name = ""

                try:
                    first_name = " ".join([n.capitalize() for n in row["First Name"].split()])
                except:
                    first_name = ""

                vcard_file.write('BEGIN:VCARD\n')
                vcard_file.write('VERSION:3.0\n')
                vcard_file.write(f'N:{last_name} - {row["Group"]};{first_name};;;\n')
                vcard_file.write(f'FN:{first_name} {last_name}\n')
                vcard_file.write(f'EMAIL:{row["Email"].lower()}\n')
                vcard_file.write(f'TEL:{row["Phone Number"]}\n')
                vcard_file.write(f'CATEGORIES:{row["Group"]}\n')
                vcard_file.write('END:VCARD\n')
                vcard_file.write('\n')


def main():
    csv_filename = 'contatti-grest2024.csv'
    vcard_filename = 'contacts.vcf'

    csv_to_vcard(csv_filename, vcard_filename)
    print(f'vCard file {vcard_filename} has been created.')


if __name__ == '__main__':
    main()
