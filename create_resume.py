from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Register Chinese font (use system font)
try:
    pdfmetrics.registerFont(TTFont('SimHei', 'C:\\Windows\\Fonts\\simhei.ttf'))
    pdfmetrics.registerFont(TTFont('SimSun', 'C:\\Windows\\Fonts\\simsun.ttc'))
    FONT_CHINESE = 'SimHei'
except:
    FONT_CHINESE = 'Helvetica'

c = canvas.Canvas("简历.pdf", pagesize=A4)
width, height = A4

# Colors
DARK_BLUE = colors.HexColor('#1a365d')
LIGHT_BLUE = colors.HexColor('#2b6cb0')
GRAY = colors.HexColor('#718096')
LIGHT_GRAY = colors.HexColor('#e2e8f0')

# Header
c.setFillColor(DARK_BLUE)
c.rect(0, height - 80, width, 80, fill=1, stroke=0)

# Name
c.setFillColor(colors.white)
c.setFont(FONT_CHINESE, 32)
c.drawString(30*mm, height - 50*mm, "唐靖东")

# Contact info
c.setFont(FONT_CHINESE, 11)
c.setFillColor(colors.HexColor('#e2e8f0'))
c.drawString(30*mm, height - 62*mm, "15975309915  |  tangjingdong0301@163.com")

# Section function
def draw_section(title, y):
    c.setStrokeColor(LIGHT_BLUE)
    c.setLineWidth(2)
    c.line(20*mm, y + 5*mm, 30*mm, y + 5*mm)
    c.setFillColor(DARK_BLUE)
    c.setFont(FONT_CHINESE, 14)
    c.drawString(32*mm, y, title)
    return y - 10*mm

def draw_job_title(title, period, y):
    c.setFillColor(DARK_BLUE)
    c.setFont(FONT_CHINESE, 13)
    c.drawString(20*mm, y, title)
    c.setFillColor(GRAY)
    c.setFont(FONT_CHINESE, 10)
    c.drawRightString(width - 20*mm, y, period)
    return y - 8*mm

def draw_bullet(text, y):
    c.setFillColor(LIGHT_BLUE)
    c.circle(25*mm, y - 2*mm, 2*mm, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#2d3748'))
    c.setFont(FONT_CHINESE, 10)
    # Wrap text
    lines = []
    words = text.split()
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line else word
        if c.stringWidth(test_line, FONT_CHINESE, 10) < 140*mm:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    for i, line in enumerate(lines):
        c.drawString(32*mm, y - i*5*mm, line)
    return y - len(lines)*5*mm - 8*mm

# Work Experience Section
y = height - 110*mm
y = draw_section("工作经历", y)

# WPS AI
y = draw_job_title("金山办公 | WPS AI产品经理", "2023.12 - 至今", y)
y = draw_bullet("PC端侧边栏-文字AI助手：从0到1设计，26年将成为WPS AI核心方向，覆盖亿级用户", y)
y = draw_bullet("灵犀智能助理-Web端：文档生成/编辑/Canvas，AI原生产品", y)

y -= 5*mm
# 账号中台+B端
y = draw_job_title("金山办公 | 账号产品经理 → B端产品经理", "2020.07 - 2023.11", y)
y = draw_bullet("账号中台：主导全产品线账号隔离改造，从单账号升级为多账号体系，完成26个方案设计", y)
y = draw_bullet("账号通讯录模块：企业账号全生命周期管理，对接飞书/钉钉/企业微信", y)
y = draw_bullet("数据安全模块：从0到1落地明水印/暗水印/密级/DLP，通威/新东方标杆客户", y)

y -= 5*mm
# 电信
y = draw_job_title("中国电信 | 天翼数字生活 | 产品经理", "2019.07 - 2021.07", y)
y = draw_bullet("189邮箱：从0搭建用户标签系统，转化率不变情况下营销量减少40%", y)
y = draw_bullet("服务号后台：覆盖全国31省，每月约100万次广告点击量", y)

# Education
y -= 5*mm
y = draw_section("教育背景", y)
c.setFillColor(colors.HexColor('#2d3748'))
c.setFont(FONT_CHINESE, 11)
c.drawString(20*mm, y, "华南理工大学 | 自动化 | 本科（2015.09 - 2019.07）")

# Skills
y -= 15*mm
y = draw_section("专业技能", y)
c.setFillColor(colors.HexColor('#2d3748'))
c.setFont(FONT_CHINESE, 11)
skills = "PMP（3A）  |  英语六级  |  SQL  |  Figma  |  Claude Code  |  Cursor"
c.drawString(20*mm, y, skills)

c.save()
print("PDF created: 简历.pdf")
