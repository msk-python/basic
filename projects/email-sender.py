import os
import smtplib
from email.message import EmailMessage

try:
    with open("my-email.txt") as emailFile:
        myEmail = emailFile.read()
except FileNotFoundError as e:
    print("Email file not Found: ", e)

try:
    with open("my-email-app-pass.txt") as aapPassFile:
        myAppPass = aapPassFile.read()
except FileNotFoundError as e:
    print("App Password file not found: ", e)


def send_gmail(receiver_gmail, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(myEmail, myAppPass)
        email = EmailMessage()
        email['From'] = "MSK Institue"
        email['To'] = receiver_gmail
        email['Subject'] = subject
        email.set_content(
            'Please enable HTML to view this message.'
        )
        email.add_alternative(message, subtype='html')
        server.send_message(email)
        print("Email Sent Success.")
    except Exception as e:
        print("An error occurred: ", e)
    finally:
        server.quit()


myHTMLMessage = """
<!DOCTYPE html>
<html>
<body style="margin: 0; padding: 0; background-color: #f4f7f6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding: 30px 10px;">
        <tr>
            <td align="center">
                <!-- Main Container -->
                <table width="600" border="0" cellspacing="0" cellpadding="0" style="background-color: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    
                    <!-- Header Banner -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #2b5876 0%, #4e4376 100%); padding: 30px 40px; text-align: center;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 26px; letter-spacing: 1px;">MSK INSTITUTE</h1>
                            <p style="color: #d1d8e0; margin: 5px 0 0 0; font-size: 14px;">Empowering Future Developers</p>
                        </td>
                    </tr>

                    <!-- Body Content -->
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="color: #2c3e50; margin-top: 0; font-size: 22px;">Request for Python Demo Class</h2>
                            <p style="color: #555555; font-size: 16px; line-height: 1.6;">
                                Hello Team,
                            </p>
                            <p style="color: #555555; font-size: 16px; line-height: 1.6;">
                                I am excited to express my interest in joining your upcoming <strong style="color: #2b5876;">Python Programming Demo Class</strong>. I am eager to learn more about your curriculum, teaching methodology, and batch schedules.
                            </p>

                            <!-- Highlight Box -->
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #f8f9fa; border-left: 4px solid #4e4376; margin: 25px 0; border-radius: 4px;">
                                <tr>
                                    <td style="padding: 15px 20px;">
                                        <p style="margin: 0 0 8px 0; color: #333333; font-size: 15px;"><strong>Course Selected:</strong> Python Programming (Beginner to Advanced)</p>
                                        <p style="margin: 0 0 8px 0; color: #333333; font-size: 15px;"><strong>Session Type:</strong> Free Demo Class</p>
                                        <p style="margin: 0; color: #333333; font-size: 15px;"><strong>Status:</strong> <span style="color: #27ae60; font-weight: bold;">Awaiting Confirmation</span></p>
                                    </td>
                                </tr>
                            </table>

                            <p style="color: #555555; font-size: 16px; line-height: 1.6;">
                                Please let me know the available dates and timings for the next session. Looking forward to hearing from you soon!
                            </p>

                            <!-- Call to Action Button -->
                            <table border="0" cellspacing="0" cellpadding="0" style="margin-top: 30px;">
                                <tr>
                                    <td align="center" style="border-radius: 6px; background-color: #4e4376;">
                                        <a href="www.mskinstitute.in" style="font-size: 16px; font-weight: bold; color: #ffffff; text-decoration: none; padding: 12px 28px; display: inline-block;">Website.</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f1f2f6; padding: 20px 40px; text-align: center; border-top: 1px solid #e1e2e6;">
                            <p style="color: #7f8c8d; font-size: 13px; margin: 0;">
                                Sent via Automated Python Script &bull; <strong>MSK Institute</strong>
                            </p>
                            <p style="color: #95a5a6; font-size: 12px; margin: 5px 0 0 0;">
                                If you did not expect this request, please ignore this email.
                            </p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""

if __name__ == "__main__":
    # send_gmail('mskshikohabad@gmail.com', "Book Demo Class", "I Want to join your Python Demo Class.")
    send_gmail('mskshikohabad@gmail.com', "Book Demo Class", myHTMLMessage)

