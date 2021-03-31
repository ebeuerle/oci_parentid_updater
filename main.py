import lib
import json
import csv


class OCIParentMap():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.rl_sess = lib.RLSession(self.config.rl_user, self.config.rl_pass, self.config.rl_cust,
                                     self.config.rl_api_base)

    def get_pcs_accounts(self):
        self.url = "https://" + self.config.rl_api_base + "/cloud/name"
        self.rl_sess.authenticate_client()
        response = self.rl_sess.client.get(self.url)
        pcs_accounts_json = response.json()

        return pcs_accounts_json

    def read_csv_file(self):
        filename = self.config.rl_file_name ###<==Configure filename in configs.yml
        cloud_acct_id = []
        wholefile = []

        with open(filename,'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                wholefile.append(dict(row))
        return wholefile, csvreader.fieldnames

    def update_csv_parent_acct(self,pcs_accounts,wholefile,fields):
        filename = "alerts_updated.csv"
        fields.append('Parent Id')

        for entry in wholefile:
            for parent in pcs_accounts:
                if entry['Cloud Account Id'] == parent['id']:
                    entry.update({'Parent Id': parent['parentAccountName']})

        with open(filename, 'w') as fd:
            writer = csv.DictWriter(fd, fieldnames=fields)
            writer.writeheader()
            writer.writerows(wholefile)


    def run(self):
        pcs_accounts = self.get_pcs_accounts()
        wholefile, fieldnames = self.read_csv_file()
        self.update_csv_parent_acct(pcs_accounts,wholefile,fieldnames)

def main():
    OCI_parent_map = OCIParentMap()
    OCI_parent_map.run()

if __name__ == "__main__":
    main()
