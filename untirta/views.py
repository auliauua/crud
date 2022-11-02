from django.shortcuts import render
from untirta.models import Dosen, Staf, Mahasiswa
from untirta.forms import FormDosen 
def faperta(request):
    jurusan = ["Agribisnis", "Agroekoteknologi", "Perikanan"]
    
    konteks = {
    'title': jurusan
    }
    return render(request, 'faperta.html', konteks)

def dosen(request):
    nama = ["Dr. Cecep Anwar Hadi Firdos Santosa, M.Si.", "Agroekoteknologi", "Perikanan"]
    konteks = {
    'title': nama
    }
    return render(request, 'dosen.html', konteks)

def feb(request):
    jurusan = ["Akutansi", "Manajemen", "Ekonomi Syariah", "Ekonomi Pembangunan"]
    
    konteks = {
        'title': jurusan
    }
    return render(request, 'feb.html', konteks)

def fh(request):
    jurusan = ["Ilmu Hukum"]
    
    konteks = {
        'title': jurusan
    }
    return render(request, 'fh.html', konteks)

def fisip(request):
    jurusan = ["Ilmu Komunikasi", "Administrasi Negara", "Ilmu Pemerintahan"]
    
    konteks = {
        'title': jurusan
    }
    return render(request, 'fisip.html', konteks)

def fk(request):
    jurusan = ["Pendidikan Dokter", "Gizi", "Keperawatan", "Ilmu Keolahragaan"]
    konteks = {
        'title': jurusan
    }
    return render(request, 'fk.html', konteks)

def fkip(request):
    jurusan = ["Pendidikan Seni Drama Tari dan Musik", "Pendidikan Matematika", "Pendidikan Biologi", "Pendidikan Luar Sekolah", "Pendidikan Bahasa dan Sastra Indonesia", "Pendidikan Bahasa Inggris", "Pendidikin Anak Usia Dini (PAUD)", "Pendidikan Guru Sekolah Dasar(PGSD)", "Bimbingan dan Konseling", "Pendidikan Luar Biasa", "Pendidikan Fisika", "Pendidikan Kimia", "Pendidikan IPA", "Pendidikan Elektro", "Pendidikan Mesin", "Pendidikan Pancasila dan Kewarganegaraan (PPKN)", "Pendidikan Sosisologi", "Pendiidkan Sejarah"]
    konteks = {
        'title': jurusan
    }
    return render(request, 'fkip.html', konteks)
def ft(request):
    jurusan = ["Teknik Mesin", "Teknik Elektro", "Teknik Industri", "Teknik Metalurgi", "Teknik Kimia", "Teknik Sipil"]
    
    konteks = {
        'title': jurusan
    }
    return render(request, 'ft.html', konteks)

def pascasarjana(request):
    jurusan = ["Pendidikan Bahasa Indonesia", "Teknologi Pendidikan", "Hukum", "Administrasi Publik", "Akutansi", "Manajemen", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Ilmu Pertanian", "Ilmu Komunikasi", "Teknik Kimia", "Pendidikan Dasar", "Ekonomi"]
    
    konteks = {
        'title': jurusan
    }
    return render(request, 'pascasarjana.html', konteks)

def untirta(request):
    return render(request, 'untirta.html')

def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data Berhasil Disimpan"
            konteks = {
                'form': form, 
                'pesan' : pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)