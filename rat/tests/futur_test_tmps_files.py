"""
Tests with tmps files script.
    - get => retour 200 et réponse json
    - post => retour 201 et réponse json
    - put => retour 200 et réponse json
    - delete => retour 200 et réponse vide
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
    
    @classmethod  # <- setUpClass doit être une méthode de classe, attention !
    def setUpTestData(cls):
        Categorie.objects.create(titre="Par défaut")
    
    def setUp(self):
        self.une_variable = "Salut !"

    def test_nouveau_redirection(self):
        """ Vérifie la redirection d'un ajout d'URL """
        data = {
            'url': 'http://www.djangoproject.com',
            'pseudo': 'Jean Dupont',
        }
    
        reponse = self.client.post(reverse('mini_url.views.nouveau'), data)
        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(reponse, reverse('mini_url.views.liste'))
    
    def test_liste(self):
        """ Vérifie si une URL sauvegardée est bien affichée """

        reponse = self.client.get(reverse('mini_url.views.liste'))

        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, mini.url)
        self.assertQuerysetEqual(reponse.context['minis'], [repr(mini)])