"""Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. 
Two accounts definitely belong to the same person if there is some common email to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. 
The accounts themselves can be returned in any order."""

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        seen = set()
        bankMap = {}
        names = {}
        output = []
        for account in accounts:
            bankMap.setdefault(account[1], [])
            names[account[1]] = account[0]
            for i in range(2, len(account)):
                bankMap[account[1]].append(account[i]) 
                bankMap.setdefault(account[i], [])
                bankMap[account[i]].append(account[1])
                names[account[i]] = account[0]
        def dfs(account, group):
            if account in seen:
                return group
            else:
                seen.add(account)
                group.append(account)
                for val in bankMap[account]:
                    dfs(val, group)
        for account in accounts:
            group = [account[0]]
            dfs(account[1], group)
            if len(group) > 1:
                group = [group[0]] + sorted(group[1:])
                output.append(group)
        return output
                