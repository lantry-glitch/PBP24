website pws: http://allan-kwek-parking.pbp.cs.ui.ac.id/

untuk jawaban dari beberapa pertanyaan berikut terlampir link gdrive ini
drive: https://drive.google.com/drive/folders/1QfLorgwBiXcW8TZaz4_31kDszEZMH1G0?usp=drive_link

## Tugas 5
#### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS selector, juga dikenal sebagai specificity (spesifisitas), adalah sebagai berikut (dari yang tertinggi ke terendah):

1. **Inline Styles**: Gaya yang diterapkan langsung pada elemen HTML menggunakan atribut `style`. (misalnya style="color: blue,") 
2. **ID Selectors**: Selector yang menggunakan ID elemen (`#id`).
3. **Class Selectors, Attribute Selectors, dan Pseudo-Classes**: Selector yang menggunakan kelas (`.class`), atribut (`[attribute]`), dan pseudo-classes (`:pseudo-class`).
4. **Element Selectors dan Pseudo-Elements**: Selector yang menggunakan nama elemen (`element`) dan pseudo-elements (`::pseudo-element`).
5. **Universal Selector (`*`)**: Selector yang berlaku untuk semua elemen.

Jika ada konflik antara selector dengan spesifisitas yang sama, selector yang ditulis terakhir dalam file CSS akan digunakan.


### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Ya, karena responsive design sangat bermanfaat agar website dapat dikembangkan dan diakses pada berbagai macam jenis devices. Hal ini akan memudahkan kita dalam mengintegrasikan dan menjalankan fungsi yang sama pada satu aplikasi web untuk semua jenis devices.

- Contoh Aplikasi yang Menerapkan Responsive Design
    - **Amazon**: Situs e-commerce ini menyesuaikan tata letak dan ukuran elemen berdasarkan ukuran layar.
- Contoh Aplikasi yang Belum Menerapkan Responsive Design
    - **SiakNG**: Situs ini belum menerapkan responsive design secara sepenuhnya sehingga tulisan masih sulit terbaca oleh pengguna
  ![Screenshot 2024-10-02 102237](https://github.com/user-attachments/assets/37e71c1f-f465-4597-8238-74106b620768)

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Dalam CSS, margin, border, dan padding adalah tiga properti berbeda yang digunakan untuk mengatur ruang di sekitar elemen.
1. Margin
Definisi: margin adalah ruang di luar elemen yang memisahkan elemen dari elemen lain di sekitarnya.
Ciri: Margin bersifat transparan, tidak memiliki warna, dan tidak memengaruhi ukuran konten elemen.
contoh:
```css
.box {
    margin: 20px; /* Memberikan jarak 20px di semua sisi elemen */
}
```
2. Border
Definisi: border adalah garis yang mengelilingi elemen, yang terletak antara padding dan margin.
Ciri: Border dapat memiliki warna, ketebalan, dan gaya (seperti solid, dashed, dll).
contoh:
```css
.box {
    border: 2px solid black; /* Border hitam dengan ketebalan 2px */
}
```
3. Padding
Definisi: padding adalah ruang di dalam elemen yang memisahkan konten dari border.
Ciri: Padding juga bersifat transparan, tetapi ruangnya berada di dalam elemen, antara konten dan border.
contoh:
```css
.box {
    padding: 15px; /* Menambahkan ruang 15px di dalam elemen, antara konten dan border */
}
```

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
  1. **1. Mengimplementasi fungsi mengedit dan menghapus produk dengan menambahkan fungsi tersebut pada `views.py`.**
     Membuat function-function yang berfungsi sebagai logika mengedit dan menghapus objek produk
     ```pyhton
     def edit_park(request, id):
    # Get mood entry berdasarkan id
    park = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ParKingEntryForm(request.POST or None, instance=park)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_park.html", context)

    def delete_park(request, id):
    # Get mood berdasarkan id
    park = Product.objects.get(pk = id)
    # Hapus mood
    park.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
     ```

  2. **Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework**
Sebelum memulai menggunakan Tailwind pada project, kita perlu mengubungkan Tailwind melalui CDN (Content Distribution Network). CDN memungkinkan untuk memakai fitur styling yang disediakan oleh Tailwind tanpa perlu mendownload atau mengkonfigurasi Tailwind pada direktori projek seperti yang sudah dilakukan pada tutorial sebelumnya. Penghubungan ini dilakukan pada `base.html`. Tailwind dipanggil dengan cara:
```html
...
<meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com">
    </script>
...
```
Setelah menginisiasi Tailwind, ada beberapa component yang dikustomisasi designnya saat mengerjakan tugas ini, misalnya **Login, Register, Tambah Produk, Edit Produk, Daftar Produk, Card Product, dan lain-lain**. Berikut contoh implementasi untuk masing-masing component dapat diakses pada link-link berikut ini:
- [Login Page](https://github.com/lantry-glitch/PBP24/blob/main/main/templates/login.html)
- [Register Page](https://github.com/lantry-glitch/PBP24/blob/main/main/templates/register.html)
- [Create Product](https://github.com/lantry-glitch/PBP24/blob/main/main/templates/create_park_entry.html)
- [Edit Product](https://github.com/lantry-glitch/PBP24/blob/main/main/templates/edit_park.html)
- [Tampilan Product](https://github.com/lantry-glitch/PBP24/blob/main/main/templates/main.html)
- [Card Product](https://github.com/lantry-glitch/PBP24/blob/main/main/templates/card_park.html)
- [Navigation Bar](https://github.com/lantry-glitch/PBP24/blob/main/main/templates/navbar.html)
Semua kustomisasi dilakukan menggunakan TailwindCSS dan style dipanggil secara langsung dan inline melalui Tailwind CDN

## Tugas 4
#### 1. Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
  `HttpResponseRedirect()` hanya bisa digunakan jika kita ingin melakukan pengalihan manual ke URL tertentu. misalnya
   ```python
   from django.http import HttpResponseRedirect
      return HttpResponseRedirect('/about/')
   ```
   sedangkan `redirect()` fungsi bawaan Django yang lebih "high-level" yang dapat menerima URL lengkap, nama view, dan nama URL pattern sebagai argumen. `redirect()` juga dapat menerima argumen tambahan seperti `args` dan `kwargs`. Sehingga, `redirect()` lebih fleksibel dan dapat digunakan dalam berbagai kasus.

#### 2. Cara kerja penghubungan model Product dengan User!
   Model `Product` dan `User` dapat dihubungkan menggunakan relasi `ForeignKey`. Relasi `ForeignKey` memungkinkan satu model untuk memiliki banyak model lainnya. Dengan menggunakan relasi `ForeignKey`,
   model `Product` dapat memiliki relasi dengan model `User`.
   ```python
   class Product(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
   ```
#### 3. Cara Django mengingat pengguna yang telah login dan apakah cookies aman?
 Autentikasi dan otorisasi adalah dua komponen penting dalam sistem keamanan aplikasi web, termasuk Django.
    **Autentikasi** adalah proses verifikasi identitas pengguna. Dalam konteks Django, ini berarti memverifikasi bahwa pengguna adalah siapa yang mereka klaim. Misalnya, ketika pengguna mencoba masuk, sistem akan memeriksa apakah kombinasi nama pengguna dan kata sandi yang diberikan cocok dengan apa yang ada di database.
    **Otorisasi**, di sisi lain, menentukan apa yang diizinkan pengguna lakukan setelah mereka berhasil melewati proses autentikasi. Ini bisa berarti memeriksa apakah pengguna memiliki izin untuk mengakses halaman tertentu, atau apakah mereka diizinkan untuk melakukan tindakan tertentu (seperti mengedit atau menghapus entri database).
    Saat pengguna login, Django akan melakukan proses authentication untuk memverifikasi identitas pengguna. Setelah proses authentication berhasil, Django akan melakukan proses authorization untuk memverifikasi hak akses pengguna. Django mengimplementasikan kedua konsep tersebut dengan menggunakan `User` model dan `auth` views. `User` model digunakan untuk menyimpan informasi pengguna seperti username, password, dan email. `auth` views digunakan untuk melakukan proses authentication dan authorization. Django juga menyediakan decorator `@login_required` untuk membatasi akses pengguna yang belum login. Dengan menggunakan decorator `@login_required`, Django akan memastikan bahwa pengguna yang belum login tidak dapat mengakses halaman tertentu.


#### 4. Cara Django mengingat pengguna yang telah login dan apakah cookies aman?
  Django mengingat pengguna yang telah login dengan menggunakan session. Session adalah cara untuk menyimpan informasi pengguna di server. Django menyimpan session pengguna di database atau cache. Django juga menggunakan cookies untuk menyimpan session ID pengguna. Cookies adalah cara untuk menyimpan informasi pengguna di browser. Cookies digunakan untuk menyimpan session ID pengguna, token CSRF, dan preferensi pengguna. Tidak semua cookies aman digunakan. Cookies yang tidak aman dapat digunakan untuk melacak pengguna, menyimpan informasi sensitif, dan menyebabkan serangan XSS (Cross-Site Scripting). Oleh karena itu, developers harus berhati-hati dalam menggunakan cookies dan memastikan bahwa cookies yang digunakan aman.
  
#### 5. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

1. **Implementasi fungsi registrasi:**

    1. Pertama-tama saya jalankan virtual environment terlebih dahulu di cmd direktori saya:
    
        ```cmd
        env\Scripts\activate.bat
        ```
    
    2. Saya tambahkan import `redirect`, `UserCreationForm`, dan `messages` pada bagian paling atas pada `views.py`:
    
        ```python
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
        ```
    
    3. Saya tambahkan potongan kode berikut ke dalam fungsi `register`:
    
        ```python
        def register(request):
            form = UserCreationForm()
    
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form': form}
            return render(request, 'register.html', context)
        ```
    
    4. Saya membuat file HTML baru dengan nama `register.html` di folder `main/templates`:
    
        ```html
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}
        <div class="login">
            <h1>Register</h1>
            <form method="POST">  
                {% csrf_token %}
                <table>
                    {{ form.as_table }}
                    <tr>
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar" /></td>
                    </tr>
                </table>
            </form>
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        </div>
        {% endblock content %}
        ```

    5. Saya tambahkan path routing di `urls.py`:
    
        ```python
        from main.views import register
        
        urlpatterns = [
            ...
            path('register/', register, name='register'),
            ...
        ]
        ```

2. **Implementasi fungsi login:**

    1. Saya tambahkan import `authenticate` dan `login`:
    
        ```python
        from django.contrib.auth import authenticate, login
        ```
    2. Saya tambahkan potongan kode berikut ke dalam fungsi `login_user`:
    
        ```python
        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main:show_main')
                else:
                    messages.info(request, 'Sorry, incorrect username or password.')
            context = {}
            return render(request, 'login.html', context)
        ```

    3. Saya buat file HTML baru `login.html` di folder `main/templates`:
    
        ```html
        {% extends 'base.html' %}

        {% block meta %}
            <title>Login</title>
        {% endblock meta %}

        {% block content %}
        <div class="login">
            <h1>Login</h1>
            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
        </div>
        {% endblock content %}
        ```

    4. Saya tambahkan path routing di `urls.py`:
    
        ```python
        from main.views import login_user
        
        urlpatterns = [
            ...
            path('login/', login_user, name='login'),
            ...
        ]
        ```

            
    3. implementasi fungsi logout
        1. saya tambahkan import logout pada bagian paling atas pada views.py
            ```python
            from django.contrib.auth import logout
            ```
        2. saya tambahkan potongan kode di bawah ini ke dalam fungsi logout yang sudah saya buat sebelumnya. Potongan kode ini berfungsi untuk melakukan mekanisme logout.
            ```python
            def logout_user(request):
                logout(request)
                return redirect('main:login')
            ```
        3. saya tambahkan potongan kode di bawah ini setelah hyperlink tag untuk Add New Product pada berkas main.html
            ```html
            ...
            <a href="{% url 'main:logout' %}">
                <button>
                    Logout
                </button>
            </a>
            ...
            ```
        4. saya buka urls.py dan import fungsi yang sudah saya buat tadi
            ```python
            from main.views import logout_user
            ```
        5. saya tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
        ```python
        ...
        path('logout/', logout_user, name='logout'),
        ...
        ```
5. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
    - saya buka views.py yang ada pada subdirektori main dan tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas
    ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
    - Pada fungsi login_user, saya menambahkan fungsi untuk menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. Caranya adalah dengan mengganti kode yang ada pada blok if user is not None menjadi potongan kode berikut
    ```python
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
    - Pada fungsi show_main, saya tambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context. Berikut adalah contoh kode yang sudah diubah.
    ```python
    context = {
        'name': request.user.username,
        'class': 'PBP F',
        'aplikasi': 'ParKing',
        'slogan': 'Rule Your Parking Experience',
        'deskripsi': 'aplikasi review dan live-update kondisi ketersediaan tempat parkir beserta harganya',
        'park_entries': park_entries,
        'last_login': request.COOKIES['last_login'],
    }
    ```
    - saya mengubah fungsi logout_user menjadi seperti potongan kode berikut
    ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    - saya Buka berkas main.html dan tambahkan potongan kode berikut di antara tabel dan tombol logout untuk menampilkan data last login.
    ```html
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```
    
5. Menghubungkan model Product dengan User
    - saya buka models.py yang ada pada subdirektori main dan tambahkan kode berikut pada dibawah kode untuk mengimpor model:
    ```python
    ...
    from django.contrib.auth.models import User
    ...
    ```
    - Pada model Product yang sudah dibuat, saya tambahkan potongan kode berikut
    ```python
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
    - saya buka views.py yang ada pada subdirektori main, dan ubah potongan kode pada fungsi create_product menjadi sebagai berikut:
    ```python
    form = ParKingEntryForm(request.POST or None, request.FILES)

    if form.is_valid() and request.method == "POST":
        park_entry = form.save(commit=False)
        park_entry.user = request.user
        park_entry.save()
        return redirect('main:show_main')
    ```
    - saya ubah fungsi show_main menjadi sebagai berikut
    ```python
    park_entries = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        ...
    ...
    ```
    - saya simpan semua perubahan, dan lakukan migrasi model dengan python manage.py makemigrations
    - kemudian saya lakukan python manage.py migrate untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.

5. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
    - pertama tama saya jalankan django dengan perintah 
    ```cmd
    python manage.py runserver
    ```
    - kemudian saya buat akun disana
    - kemudian saya login ke akun pertama dan menambahkan 4 data
   ![image](https://github.com/user-attachments/assets/996c3e5b-7abe-4c64-8237-65494cb8a174)

    - terakhir saya login ke akun kedua dan menambahkan 3 data
   ![image](https://github.com/user-attachments/assets/61eb270c-dee8-454e-97f2-c6077cb8f63e)
