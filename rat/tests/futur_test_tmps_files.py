"""
Tests with tmps files script.
    - get => retour 200 et r�ponse json
    - post => retour 201 et r�ponse json
    - put => retour 200 et r�ponse json
    - delete => retour 200 et r�ponse vide
    - post bidon (json pourri) => CR <=> 0
    - put bidon => CR <=> 0
    - delete bidon => CR <=> 0
    - appel ressource bidon => Popen en erreur
    - appel  

"""

from django.test import TestCase
from django.core.urlresolvers import reverse

from rat.views import RessourcesList

class TmpsTestsGet(TestCase):
    
    @classmethod  # <- setUpClass doit �tre une m�thode de classe, attention !
    def setUpTestData(cls):
        Categorie.objects.create(titre="Par d�faut")
    
    def setUp(self):
        self.une_variable = "Salut !"

    def test_nouveau_redirection(self):
        """ V�rifie la redirection d'un ajout d'URL """
        data = {
            'url': 'http://www.djangoproject.com',
            'pseudo': 'Jean Dupont',
        }
    
        reponse = self.client.post(reverse('mini_url.views.nouveau'), data)
        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(reponse, reverse('mini_url.views.liste'))
    
    def test_liste(self):
        """ V�rifie si une URL sauvegard�e est bien affich�e """

        reponse = self.client.get(reverse('mini_url.views.liste'))

        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, mini.url)
        self.assertQuerysetEqual(reponse.context['minis'], [repr(mini)])