import subprocess

# رابط الفيديو .TS (ملف Transport Stream)
source_ts = "http://ugeen.live:8080/Ugeen_VIPAjNtEA/mNFuQn/3875"

# رابط RTMP (إدخال مفتاح البث الخاص بك)
rtmp_url = "rtmp://istanbul.castr.io/static/live_0ba5e570ad8211ef8d04e98c51c128c2?password=4fa8bff2"

# المستخدم يدخل الفريمات والدقة
frame_rate = 25  # الفريمات
resolution = "400x360"  # دقة البث

# مسار الصورة التي ستستخدم كحقوق (Watermark)
watermark_image = "http://assets.tkoen.co4.in/tkoen%C3%97rsr.png"  # ضع مسار الصورة هنا

# النص المطلوب إضافته
custom_text = "لمشاهدة جميع المباريات على تطبيق RsR tv"

# استخدام FFmpeg لبث الفيديو مع حقوق ونص في أسفل وسط الشاشة
ffmpeg_command = [
    "ffmpeg", "-re", "-i", source_ts,
    "-i", watermark_image,  # إدخال الصورة
    "-filter_complex", (
        "[1:v]scale=250:250[wm];"  # تغيير حجم الصورة
        "[0:v][wm]overlay=W-w-10:20,drawtext=fontfile=/path/to/font.ttf:"  # إضافة الصورة في أعلى يمين الشاشة
        f"text='{custom_text}':fontcolor=white:fontsize=24:x=(W-tw)/2:y=H-th-30"  # النص في أسفل وسط الشاشة
    ),
    "-c:v", "libx264", "-preset", "ultrafast",
    "-r", str(frame_rate),  # تحديد الفريمات
    "-s", resolution,  # تحديد الدقة
    "-b:v", "1400k", "-c:a", "aac", "-b:a", "64k", "-f", "flv", rtmp_url
]

# تشغيل FFmpeg للبث
try:
    print(f"Starting to stream to {rtmp_url} with resolution {resolution}, {frame_rate} FPS, watermark, and custom text...")
    subprocess.run(ffmpeg_command)
    print("Streaming started with watermark and text...")
except Exception as e:
    print(f"Error: {e}")
