from django.shortcuts import render, redirect

# Create your views here.
from . models import Absen
from . forms import AbsenForm

def update(request, update_id):
    data_update = Absen.objects.get(id=update_id)

    data = {
        'nama_depan':data_update.nama_depan,
        'nama_belakang': data_update.nama_belakang,
        'kelas':data_update.kelas,
        'jurusan':data_update.jurusan,
        'alamat':data_update.alamat,
    }

    absen_form = AbsenForm(request.POST or None, initial=data, instance=data_update)
    if request.method == 'POST':
        if absen_form.is_valid():
            absen_form.save()
        return redirect('absen:list')
    context = {
        'page_title':'Ubah Data Siswa',
        'absen_form':absen_form,
    }
    return render(request,'absen/create.html',context)

def delete(request, delete_id):
    Absen.objects.filter(id=delete_id).delete()
    return redirect('absen:list')

def create(request):
    absen_form = AbsenForm(request.POST or None)

    if request.method == 'POST':
        if absen_form.is_valid():
            absen_form.save()
        return redirect('absen:list')

    context = {
        'page_title':'Tambah Data Siswa',
        'absen_form':absen_form,
    }

    return render(request, 'absen/create.html', context)

def list(request):
    semua_data = Absen.objects.all()

    context = {
        'page_title':'Tabel Data Siswa',
        'semua_data':semua_data,
    }

    return render(request, 'absen/list.html', context)
