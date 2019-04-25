def get_gtoken(skey):
        hash_val=5381
        for i in range(0, len(skey)):
            hash_val += (hash_val << 5)+ord(skey[i])
        return hash_val&0x7fffffff


app_id = 0


secret_id = ""
secret_key = ""
uin = ""

skey = ''

sub_secret_id = ""
sub_secret_key = ""
sub_uin = ""


csrfCode = get_gtoken(skey)
cookie = "uin=o" + uin + "; skey=" + skey

