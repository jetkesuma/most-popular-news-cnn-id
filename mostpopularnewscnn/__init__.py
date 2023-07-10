import requests
import bs4


class Mostpopularnewscnn:
    def __init__(self):
        self.description = 'to get the most popular news in cnnindonesia.com'
        self.result = None

    def data_extraction(self):
        try:
            content = requests.get('https://www.cnnindonesia.com/')
        except Exception:
            return None
        if content.status_code == 200:
            soup = bs4.BeautifulSoup(content.text, 'html.parser')
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

            self.result = result
        else:
            return None


    def show_data(self):
        if self.result is None:
            print("Cant Show data")
            return

        print('\nMost Popular News at CNN Indonesia Update')
        print(f"Most Popular News at CNN Indonesia Number 1 is {self.result['numberone']}")
        print(f"Most Popular News at CNN Indonesia number 2 is {self.result['numbertwo']}")
        print(f"Most Popular News at CNN Indonesia number 3 is {self.result['numberthree']}")
        print(f"Most Popular News at CNN Indonesia number 4 is {self.result['numberfour']}")
        print(f"Most Popular News at CNN Indonesia number 5 is {self.result['numberfive']}")
        print(f"Most Popular News at CNN Indonesia number 6 is {self.result['numbersix']}")

    def run (self):
        self.data_extraction()
        self.show_data()


if __name__ == '__main__':
    most_popular_news_cnn_id = Mostpopularnewscnn()
    print('Description class news cnn id', most_popular_news_cnn_id.description)
    most_popular_news_cnn_id.run()
    # most_popular_news_cnn_id.data_extraction()
    # most_popular_news_cnn_id.show_data()
