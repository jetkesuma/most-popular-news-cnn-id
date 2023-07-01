import requests
from bs4 import BeautifulSoup


def data_extraction():
    """
    1. SBY tidak masalah jika Jokowi tidak suka dengan anies baswedan
    2. Video: Bangunan 13 lantai Runtuh di Mesir, 4 Orang Terluka
    3. Prabowo mendadak dipanggil jokowi, Gelar pertemuan Tertutup di Istana
    4. Surya Paloh yakin anies tak akan jadi tersangka jelang pilpres 2024
    5. Bahas Politik, Prabowo ditanya jokowi soal rencana ke depan
    6. Erick thohir Ungkap kekurangan JIS untuk Venue Piala Dunia U-175
    :return:
    """
    try:
        content = requests.get('https://www.cnnindonesia.com/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        oke = soup.find('div', {'class': 'headline__terpopuler-list'})
        oke = oke.findChildren('article')
        i = 0
        numberone = None
        numbertwo = None
        numberthree = None
        numberfour = None
        numberfive = None
        numbersix = None
        for res in oke:
            # print(i, res)
            if i == 0:
                numberone = res.text
            elif i == 1:
                numbertwo = res.text
            elif i == 2:
                numberthree = res.text
            elif i == 3:
                numberfour = res.text
            elif i == 4:
                numberfive = res.text
            elif i == 5:
                numbersix = res.text
            i = i + 1

        result = dict()
        result['numberone'] = numberone
        result['numbertwo'] = numbertwo
        result['numberthree'] = numberthree
        result['numberfour'] = numberfour
        result['numberfive'] = numberfive
        result['numbersix'] = numbersix

        return result
    else:
        return None


def show_data(result):
    if result is None:
        print("Cant Show data")
        return
    print('\nMost Popular News at CNN Indonesia Update')
    print(f"Most Popular News at CNN Indonesia Number 1 is {result['numberone']}")
    print(f"Most Popular News at CNN Indonesia number 2 is {result['numbertwo']}")
    print(f"Most Popular News at CNN Indonesia number 3 is {result['numberthree']}")
    print(f"Most Popular News at CNN Indonesia number 4 is {result['numberfour']}")
    print(f"Most Popular News at CNN Indonesia number 5 is {result['numberfive']}")
    print(f"Most Popular News at CNN Indonesia number 6 is {result['numbersix']}")

if __name__ == '__main__':
    result = data_extraction()
    show_data(result)