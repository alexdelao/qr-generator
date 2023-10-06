from django.shortcuts import render
import qrcode
from io import BytesIO
from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import QRCode

def generate_qr(request):
    if request.method == 'POST':
        url = request.POST['url']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_file = InMemoryUploadedFile(img_io, None, f'qr_code.png', 'image/png', img_io.getbuffer().nbytes, None)
        qr_code = QRCode(url=url, qr_image=img_file)
        qr_code.save()

        return redirect('show_qr', pk=qr_code.pk)
    return render(request, 'qrgenerator/generate_qr.html')

def show_qr(request, pk):
    qr_code = QRCode.objects.get(pk=pk)
    return render(request, 'qrgenerator/show_qr.html', {'qr_code': qr_code})
