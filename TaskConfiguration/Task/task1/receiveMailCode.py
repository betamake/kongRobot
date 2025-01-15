import imaplib
import poplib
import email
from email.header import decode_header

# Outlook IMAP服务器地址和端口
IMAP_SERVER = 'outlook.office365.com'
IMAP_PORT = 993

# Outlook POP3服务器地址和端口
POP3_SERVER = 'outlook.office365.com'
POP3_PORT = 995

def clean(text):
    # 清理字符串，以防有非法文件系统字符
    return "".join(c if c.isalnum() else "_" for c in text)

def get_verification_code(EMAIL_ACCOUNT, PASSWORD):
    # 先尝试使用 IMAP 登录
    try:
        code = get_verification_code_imap(EMAIL_ACCOUNT, PASSWORD, "inbox")
        if code:
            return code
    except Exception as e:
        print(f"IMAP登录失败（收件箱）: {str(e)}")
    
    # 如果收件箱没有找到，切换到垃圾邮件文件夹
    try:
        code = get_verification_code_imap(EMAIL_ACCOUNT, PASSWORD, "Junk Email")
        if code:
            return code
    except Exception as e:
        print(f"IMAP登录失败（垃圾邮件）: {str(e)}")
    
    # 如果 IMAP 登录失败，尝试使用 POP3
    try:
        code = get_verification_code_pop3(EMAIL_ACCOUNT, PASSWORD)
        if code:
            return code
    except Exception as e:
        print(f"POP3登录失败: {str(e)}")
    
    return None

def get_verification_code_imap(EMAIL_ACCOUNT, PASSWORD, folder):
    # 使用 IMAP 登录并获取验证码
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL_ACCOUNT, PASSWORD)
        mail.select(folder)
        
        _, search_data = mail.search(None, 'ALL')
        
        for num in search_data[0].split():
            _, data = mail.fetch(num, '(RFC822)')
            _, b = data[0]
            email_message = email.message_from_bytes(b)
            
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    code = extract_code(body)
                    if code:
                        return code
    except Exception as e:
        raise e
    finally:
        mail.logout()
    
    return None

def get_verification_code_pop3(EMAIL_ACCOUNT, PASSWORD):
    # 使用 POP3 登录并获取验证码
    try:
        pop_server = poplib.POP3_SSL(POP3_SERVER, POP3_PORT)
        pop_server.user(EMAIL_ACCOUNT)
        pop_server.pass_(PASSWORD)
        
        num_messages = len(pop_server.list()[1])
        print("+++++++++",email_message)
        for i in range(num_messages, 0, -1):
            raw_email = b"\n".join(pop_server.retr(i)[1])
            email_message = email.message_from_bytes(raw_email)
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    code = extract_code(body)
                    if code:
                        return code
    except Exception as e:
        raise e
    finally:
        pop_server.quit()
    
    return None

def extract_code(body):
    # 从邮件内容中提取验证码
    match = re.search(r'\b\d{6}\b', body)
    if match:
        return match.group(0)  # 返回找到的验证码
    return None  # 如果没有找到任何匹配，返回None

# 示例用法：
EMAIL_ACCOUNT = 'twuff@outlook.com'
PASSWORD = 'GNfw9864'
verification_code = get_verification_code(EMAIL_ACCOUNT, PASSWORD)
if verification_code:
    print("Verification Code:", verification_code)
else:
    print("No verification code found.")
