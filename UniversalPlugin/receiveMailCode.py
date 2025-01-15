import imaplib
import email
from email.header import decode_header

# Outlook IMAP服务器地址和端口
IMAP_SERVER = 'outlook.office365.com'
IMAP_PORT = 993

# 邮箱账户和密码
EMAIL_ACCOUNT = 'zzzzqqq66668888@outlook.com'
PASSWORD = 'Chen6170858..'

def clean(text):
    # 清理字符串，以防有非法文件系统字符
    return "".join(c if c.isalnum() else "_" for c in text)

def get_verification_code():
    # 连接到IMAP服务器
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    
    # 登录到邮箱
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    
    # 选择收件箱
    mail.select("inbox")
    
    # 搜索包含特定关键词的邮件
    status, messages = mail.search(None, 'ALL')
    
    # 将消息ID分隔成列表
    email_ids = messages[0].split()
    
    # 遍历所有邮件，从最新的开始
    for email_id in reversed(email_ids):
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
                
                # 打印邮件主题
                print("Subject:", subject)
                
                # 初始化 body 变量
                body = ""
                
                # 解析邮件内容
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        
                        if "verification code" in body:
                            print("Found verification code in email:")
                            print(body)
                            # 提取验证码
                            code = extract_code(body)
                            return code
                else:
                    content_type = msg.get_content_type()
                    
                    try:
                        body = msg.get_payload(decode=True).decode()
                    except:
                        pass
                    
                    if "verification code" in body:
                        print("Found verification code in email:")
                        print(body)
                        # 提取验证码
                        code = extract_code(body)
                        return code
    
    mail.logout()
    return None

def extract_code(body):
    # 从邮件内容中提取验证码
    import re
    match = re.search(r'Your Link verification code is:\s*(\d+)', body)
    if match:
        return match.group(1)
    return None

# 示例用法
# verification_code = get_verification_code()
# if verification_code:
#     print("Verification Code:", verification_code)
# else:
#     print("No verification code found.")
