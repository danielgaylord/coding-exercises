class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        res = {}
        for account in accounts:
            acc_name = account[0]           
            acc_emails = [set(account[1:])]
            if acc_name in res:
                email_lists = res[acc_name]
                for emails in email_lists:
                    if not acc_emails[0].isdisjoint(emails):
                        acc_emails[0] = acc_emails[0].union(emails)
                    else:
                        acc_emails.append(emails)                        
                res[acc_name] = acc_emails
            else:
                res.update({acc_name: acc_emails})
        return [[name] + sorted(list(email)) for name, emails in res.iteritems() for email in emails]