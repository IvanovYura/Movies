FILMS = [
    {
        'id': '0440483e-ca0e-4120-8c50-4c8cd9b965d6',
        'title': 'Castle in the Sky',
        'description': 'The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom '
                       'of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, '
                       'she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit '
                       'the evil Muska, who plans to use Laputa\'s science to make himself ruler of the world.',
        'director': 'Hayao Miyazaki',
        'producer': 'Isao Takahata',
        'release_date': '1986',
        'rt_score': '95',
        'people': [
            'https://ghibliapi.herokuapp.com/people/'
        ],
        'species': [
            'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2'
        ],
        'locations': [
            'https://ghibliapi.herokuapp.com/locations/'
        ],
        'vehicles': [
            'https://ghibliapi.herokuapp.com/vehicles/'
        ],
        'url': 'https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe'
    },
    {
        'id': '58611129-2dbc-4a81-a72f-77ddfc1b1b49',
        'title': 'Grave of the Fireflies',
        'description': 'In the latter part of World War II, a boy and his sister, orphaned when their mother is '
                       'killed in the firebombing of Tokyo, are left to survive on their own in what remains of '
                       'civilian life in Japan. The plot follows this boy and his sister as they do their best to '
                       'survive in the Japanese countryside, battling hunger, prejudice, and pride in their own '
                       'quiet, personal battle.',
        'director': 'Isao Takahata',
        'producer': 'Toru Hara',
        'release_date': '1988',
        'rt_score': '97',
        'people': [
            'https://ghibliapi.herokuapp.com/people/'
        ],
        'species': [
            'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2'
        ],
        'locations': [
            'https://ghibliapi.herokuapp.com/locations/'
        ],
        'vehicles': [
            'https://ghibliapi.herokuapp.com/vehicles/'
        ],
        'url': 'https://ghibliapi.herokuapp.com/films/12cfb892-aac0-4c5b-94af-521852e46d6a'
    },
    {
        'id': '1b67aa9a-2e4a-45af-ac98-64d6ad15b16c',
        'title': 'Pom Poko',
        'description': 'As the human city development encroaches on the raccoon population\'s forest and meadow '
                       'habitat, the raccoons find themselves faced with the very real possibility of extinction. In '
                       'response, the raccoons engage in a desperate struggle to stop the construction and preserve '
                       'their home.',
        'director': 'Isao Takahata',
        'producer': 'Toshio Suzuki',
        'release_date': '1994',
        'rt_score': '78',
        'people': [
            'https://ghibliapi.herokuapp.com/people/'
        ],
        'species': [
            'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2'
        ],
        'locations': [
            'https://ghibliapi.herokuapp.com/locations/'
        ],
        'vehicles': [
            'https://ghibliapi.herokuapp.com/vehicles/'
        ],
        'url': 'https://ghibliapi.herokuapp.com/films/1b67aa9a-2e4a-45af-ac98-64d6ad15b16c'
    },
    {
        'id': 'ff24da26-a969-4f0e-ba1e-a122ead6c6e3',
        'title': 'Whisper of the Heart',
        'description': 'Shizuku lives a simple life, dominated by her love for stories and writing. One day she '
                       'notices that all the library books she has have been previously checked out by the same '
                       'person: "Seiji Amasawa". Curious as to who he is, Shizuku meets a boy her age whom she finds '
                       'infuriating, but discovers to her shock that he is her "Prince of Books". As she grows closer '
                       'to him, she realises that he merely read all those books to bring himself closer to her. The '
                       'boy Seiji aspires to be a violin maker in Italy, and it is his dreams that make Shizuku '
                       'realise that she has no clear path for her life.',
        'director': 'Yoshifumi Kondō',
        'producer': 'Toshio Suzuki',
        'release_date': '1995',
        'rt_score': '91',
        'people': [
            'https://ghibliapi.herokuapp.com/people/'
        ],
        'species': [
            'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2'
        ],
        'locations': [
            'https://ghibliapi.herokuapp.com/locations/'
        ],
        'vehicles': [
            'https://ghibliapi.herokuapp.com/vehicles/'
        ],
        'url': 'https://ghibliapi.herokuapp.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3'
    },
]

PEOPLE = [
    {
        'id': 'ba924631-068e-4436-b6de-f3283fa848f0',
        'name': 'Ashitaka',
        'gender': 'Male',
        'age': 'late teens',
        'eye_color': 'Brown',
        'hair_color': 'Brown',
        # one film per person
        'films': [
            'https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6'
        ],
        'species': 'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2',
        'url': 'https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0'
    },
    {
        'id': 'ebe40383-aad2-4208-90ab-698f00c581ab',
        'name': 'San',
        'gender': 'Female',
        'age': '17',
        'eye_color': 'Brown',
        'hair_color': 'Brown',
        # one film per person
        'films': [
            'https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6'
        ],
        'species': 'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2',
        'url': 'https://ghibliapi.herokuapp.com/people/ebe40383-aad2-4208-90ab-698f00c581ab'
    },
    {
        'id': '3031caa8-eb1a-41c6-ab93-dd091b541e11',
        'name': 'Tatsuo Kusakabe',
        'gender': 'Male',
        'age': '37',
        'eye_color': 'Brown',
        'hair_color': 'Dark Brown',
        # one film per person
        'films': [
            'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49'
        ],
        'species': 'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2',
        'url': 'https://ghibliapi.herokuapp.com/people/3031caa8-eb1a-41c6-ab93-dd091b541e11'
    },
    {
        'id': '116bfe1b-3ba8-4fa0-8f72-88537a493cb9',
        'name': 'Hii-sama',
        'gender': 'Female',
        'age': 'Over 50',
        'eye_color': 'Brown',
        'hair_color': 'White',
        # multiple films per person
        'films': [
            'https://ghibliapi.herokuapp.com/films/1b67aa9a-2e4a-45af-ac98-64d6ad15b16c',
            'https://ghibliapi.herokuapp.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3',
        ],
        'species': 'https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2',
        'url': 'https://ghibliapi.herokuapp.com/people/116bfe1b-3ba8-4fa0-8f72-88537a493cb9'
    },
]

OUTPUT = [
    {
        'id': '0440483e-ca0e-4120-8c50-4c8cd9b965d6',
        'title': 'Castle in the Sky',
        'description': 'The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom '
                       'of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, '
                       'she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit '
                       'the evil Muska, who plans to use Laputa\'s science to make himself ruler of the world.',
        'director': 'Hayao Miyazaki',
        'producer': 'Isao Takahata',
        'release_date': '1986',
        'rt_score': '95',
        'people': [
            {
                'id': 'ba924631-068e-4436-b6de-f3283fa848f0',
                'name': 'Ashitaka',
                'gender': 'Male',
                'eye_color': 'Brown',
                'hair_color': 'Brown',
                'age': 'late teens'
            }, {
                'id': 'ebe40383-aad2-4208-90ab-698f00c581ab',
                'name': 'San',
                'gender': 'Female',
                'eye_color': 'Brown',
                'hair_color': 'Brown',
                'age': '17'
            },
        ],
    }, {
        'id': '58611129-2dbc-4a81-a72f-77ddfc1b1b49',
        'title': 'Grave of the Fireflies',
        'description': 'In the latter part of World War II, a boy and his sister, orphaned when their mother is '
                       'killed in the firebombing of Tokyo, are left to survive on their own in what remains of '
                       'civilian life in Japan. The plot follows this boy and his sister as they do their best to '
                       'survive in the Japanese countryside, battling hunger, prejudice, and pride in their own '
                       'quiet, personal battle.',
        'director': 'Isao Takahata',
        'producer': 'Toru Hara',
        'release_date': '1988',
        'rt_score': '97',
        'people': [
            {
                'id': '3031caa8-eb1a-41c6-ab93-dd091b541e11',
                'name': 'Tatsuo Kusakabe',
                'gender': 'Male',
                'eye_color': 'Brown',
                'hair_color': 'Dark Brown',
                'age': '37'
            },
        ],
    },
    {
        'id': '1b67aa9a-2e4a-45af-ac98-64d6ad15b16c',
        'title': 'Pom Poko',
        'description': 'As the human city development encroaches on the raccoon population\'s forest and meadow '
                       'habitat, the raccoons find themselves faced with the very real possibility of extinction. In '
                       'response, the raccoons engage in a desperate struggle to stop the construction and preserve '
                       'their home.',
        'director': 'Isao Takahata',
        'producer': 'Toshio Suzuki',
        'release_date': '1994',
        'rt_score': '78',
        'people': [
            {
                'id': '116bfe1b-3ba8-4fa0-8f72-88537a493cb9',
                'name': 'Hii-sama',
                'gender': 'Female',
                'eye_color': 'Brown',
                'hair_color': 'White',
                'age': 'Over 50',
            },
        ],
    },
    {
        'id': 'ff24da26-a969-4f0e-ba1e-a122ead6c6e3',
        'title': 'Whisper of the Heart',
        'description': 'Shizuku lives a simple life, dominated by her love for stories and writing. One day she '
                       'notices that all the library books she has have been previously checked out by the same '
                       'person: "Seiji Amasawa". Curious as to who he is, Shizuku meets a boy her age whom she finds '
                       'infuriating, but discovers to her shock that he is her "Prince of Books". As she grows closer '
                       'to him, she realises that he merely read all those books to bring himself closer to her. The '
                       'boy Seiji aspires to be a violin maker in Italy, and it is his dreams that make Shizuku '
                       'realise that she has no clear path for her life.',
        'director': 'Yoshifumi Kondō',
        'producer': 'Toshio Suzuki',
        'release_date': '1995',
        'rt_score': '91',
        'people': [
            {
                'id': '116bfe1b-3ba8-4fa0-8f72-88537a493cb9',
                'name': 'Hii-sama',
                'gender': 'Female',
                'eye_color': 'Brown',
                'hair_color': 'White',
                'age': 'Over 50',
            },
        ],
    },
]
