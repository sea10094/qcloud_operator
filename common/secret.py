def get_gtoken(skey):
        hash_val=5381
        for i in range(0, len(skey)):
            hash_val += (hash_val << 5)+ord(skey[i])
        return hash_val&0x7fffffff


app_id = 251000710


secret_id = "AKID1agWVShCU7cQxKh33n9w98kw3SHhg5Pv"
secret_key = "7v64T1gUSB8hCazvDJUWxVHZzBJjbRBz"
uin = "3374998458"

skey = ''

sub_secret_id = ""
sub_secret_key = ""
sub_uin = ""


csrfCode = get_gtoken(skey)
cookie = "uin=o" + uin + "; skey=" + skey

