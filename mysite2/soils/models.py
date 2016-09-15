from django.db import models

# Create your models here.
#CREATE A SYSTEM WHICH ALLOWS SOIL SCIENTISTS TO "KEY OUT SOILS" DIGITALLY AND KEEP A LOG/VERSION CONTROL AND UPLOAD PICTURES  BASED ON THE KEY
#FIGURE OUT A WAY TO programmatically populate the database tables from the models?
class Soil(models.Model):

    # order = models.CharField(max_length=100, blank=True)
    # sub_order = models.CharField(max_length=100, blank=True)
    # great_group = models.CharField(max_length=100, blank=True)
    # sub_group = models.CharField(max_length=100, blank=True)
    # family = models.CharField(max_length=100, blank=True)
    # series = models.CharField(max_length=100, blank=True)
    # phase = models.CharField(max_length=100, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.order

class SoilOrders(models.Model):
    #list of formative elements and corresponding Soil Orders
    ents = 'Entisols'
    epts = 'Inceptisols'
    ands = 'Andisols'
    els  = 'Gelisols'
    ists = 'Histosols'
    ids  = 'Aridisols'
    erts = 'Vertisols'
    ols  = 'Mollisols'
    alfs = 'Alfisols'
    ods  = 'Spodosols'
    ults = 'Utilisols'
    ox   = 'Oxisols'
    #list of tuples allowing instances to be created w/ a dropdown select
    orders = ((ents,'Entisols'), (epts,'Inceptisols'), (ands,'Andisols'),(els,'Gelisols'),(ists,'Histosols'),
            (ids,'Aridisols'),(erts,'Vertisols'),(ols,'Mollisols'),(alfs,'Alfisols'),(ods,'Spodosols'),(ults,'Ultisols'),(ox,'Oxisols'))

    order = models.CharField(max_length=20, choices=orders, unique=True) #
    order_text = models.CharField(max_length=200, null=True, blank=True)
    #Somehow use multi-table inheritence to "programmatically create" soil taxonomy


    def __str__(self):
               # __unicode__ on Python 2
        return self.order

class SubOrders(models.Model):
    sub_orders = (
      ('Entisols', (
              ('Aquents', 'Aquents'),
              ('Fluvents', 'Fluvents'),
              ('Orthents', 'Orthents'),
              ('Psamments', 'Psamments'),
              ('Wassents', 'Wassents'),
          )
      ),
      ('Inceptisols', (
              ('Aquepts', 'Aquepts'),
              ('Cryepts', 'Cryepts'),
              ('Gelepts', 'Gelepts'),
              ('Udepts', 'Udepts'),
              ('Ustepts', 'Ustepts'),
              ('Xerepts', 'Xerepts'),
          )
      ),
      ('Andisols', (
              ('Aquands', 'Aquands'),
              ('Cryands', 'Cryands'),
              ('Gelands', 'Gelands'),
              ('Torrands', 'Torrands'),
              ('Udands', 'Udands'),
              ('Ustands', 'Ustands'),
              ('Vitrands', 'Vitrands'),
              ('Xerands', 'Xerands'),
          )
      ),
      ('Gelisols', (
              ('Histels', 'Histels'),
              ('Orthels', 'Orthels'),
              ('Turbels', 'Turbels'),
          )
      ),
      ('Histosols', (
              ('Fibrists', 'Fibrists'),
              ('Folists', 'Folists'),
              ('Hemists', 'Hemists'),
              ('Saprists', 'Saprists'),
              ('Wassists', 'Wassists'),
          )
      ),
      ('Aridisols', (
              ('Argids', 'Argids'),
              ('Calcids', 'Calcids'),
              ('Cambids', 'Cambids'),
              ('Cryids', 'Cryids'),
              ('Durids', 'Durids'),
              ('Gypsids', 'Gypsids'),
              ('Salids', 'Salids'),
          )
      ),
      ('Vertisols', (
              ('Aquerts', 'Aquerts'),
              ('Cryerts', 'Cryerts'),
              ('Torrerts', 'Torrerts'),
              ('Uderts', 'Uderts'),
              ('Usterts', 'Usterts'),
              ('Xererts', 'Xererts'),
          )
      ),
      ('Mollisols', (
              ('Albolls', 'Albolls'),
              ('Aquolls', 'Aquolls'),
              ('Cryolls', 'Cryolls'),
              ('Gellolls', 'Gellolls'),
              ('Rendolls', 'Rendolls'),
              ('Udolls', 'Udolls'),
              ('Ustolls', 'Ustolls'),
              ('Xerolls', 'Xerolls'),
          )
      ),
      ('Alfisols', (
              ('Aqualf', 'Aqualf'),
              ('Cryalf', 'Cryalf'),
              ('Udalf', 'Udalf'),
              ('Ustalf', 'Ustalf'),
              ('Xeralf', 'Xeralf'),
          )
      ),
      ('Spodosols', (
              ('Aquods', 'Aquods'),
              ('Cryods', 'Cryods'),
              ('Humods', 'Humods'),
              ('Orthods', 'Orthods'),
          )
      ),
      ('Ultisols', (
              ('Aquults', 'Aquults'),
              ('Humults', 'Humults'),
              ('Udults', 'Udults'),
              ('Usults', 'Usults'),
              ('Xerults', 'Xerults'),
          )
      ),
      ('Oxisols', (
              ('Aquox', 'Aquox'),
              ('Perox', 'Perox'),
              ('Torrox', 'Torrox'),
              ('Udox', 'Udox'),
              ('Ustox', 'Ustox'),
          )
      ),
      ('unknown', 'Unknown'),
    )

    order = models.ForeignKey('SoilOrders')
    suborder = models.CharField(max_length=50,choices=sub_orders, unique=True)


    def __str__(self):
               # __unicode__ on Python 2
        return self.suborder



#create function to switch between different possible suborders for each soil order
#create a function to prepend the formative element to soil_order --- possibly under def __str__(self): functioN!!!!!

# Alb	    	Presence of albic horizon
# Anthr		Modified by humans
# Aqu	    	Aquic conditions
# Ar	    	Mixed horizons
# Arg	    	Presence of argillic horizon
# Calc		Presence of a calcic horizons
# Camb		Presence of a cambic horizon
# Cry	    	Cold
# Dur	        Presence of a duripan
# Fibr		Least decomposed stage
# Fluv		Flood plain
# Fol	    	Mass of leaves
# Gyps		Presence of a gypsic horizon
# Hem	    	Intermediate stage of decomposition
# Hist		Presence of organic materials
# Hum	    	Presence of organic matter
# Orth		The common ones
# Per	    	Perudic moisture regime
# Psamm		Sandy texture
# Rend		High carbonate content
# Sal	    	Presence of a salic horizon
# Sapr		Most decomposed stage
# Torr		Torric moisture regime
# Turb		Presence of cryoturbation
# Ud	        Udic moisture regime
# Vitr		Presence of glass
# Ust	    	Ustic moisture regime
# Xer	    	Xeric moisture regime

class GreatGroups(models.Model):
#Entisols - Great Groups
    great_groups= (('Aquents', (
            ('Cryaquents', 'Cryaquents'),
            ('Endoaquents', 'Endoaquents'),
            ('Epiaquents', 'Epiaquents'),
            ('Fluvaquents', 'Fluvaquents'),
            ('Gelaquents', 'Gelaquents'),
            ('Hydraquents', 'Hydraquents'),
            ('Psammaquents', 'Psammaquents'),
            ('Sulfaquents', 'Sulfaquents'),
          )
      ),
    ('Fluvents', (
            ('Gelifluvents', 'Gelifluvents'),
            ('Cryofluvents', 'Cryofluvents'),
            ('Xerofluvents', 'Xerofluvents'),
            ('Ustifluvents', 'Ustifluvents'),
            ('Torrifluvents', 'Torrifluvents'),
            ('Udifluvents', 'Udifluvents'),
          )
      ),
    ('Orthents', (
            ('Gelorthents', 'Gelorthents'),
            ('Cryorthents', 'Cryorthents'),
            ('Torriorthents', 'Torriorthents'),
            ('Xerorthents', 'Xerorthents'),
            ('Ustorthents', 'Ustorthents'),
            ('Udorthents', 'Udorthents'),
          )
      ),
    ('Psamment', (
            ('Cryopsamments', 'Cryopsamments'),
            ('Torripsamments', 'Torripsamments'),
            ('Quartzipsamments', 'Quartzipsamments'),
            ('Ustipsamments', 'Ustipsamments'),
            ('Xeropsamments', 'Xeropsamments'),
            ('Udipsamments', 'Udipsamments'),
          )
      ),
    ('Wassents', (
            ('Frasiwassents', 'Frasiwassents'),
            ('Psammowassents', 'Psammowassents'),
            ('Sulfiwassents', 'Sulfiwassents'),
            ('Hydrowassents', 'Hydrowassents'),
            ('Fluviwassents', 'Fluviwassents'),
            ('Haplowassents', 'Haplowassents'),
          )
      ),
#Inceptisols - Great Groups
    ('Aquepts', (
            ('Cryaquepts', 'Cryaquepts'),
            ('Endoaquepts', 'Endoaquepts'),
            ('Epiaquepts', 'Epiaquepts'),
            ('Fragiaquepts', 'Fragiaquepts'),
            ('Gelaquepts', 'Gelaquepts'),
            ('Helaquepts', 'Helaquepts'),
            ('Humaquepts', 'Humaquepts'),
            ('Petraquepts', 'Petraquepts'),
            ('Sulfaquepts', 'Sulfaquepts'),
            ('Vermaquepts', 'Vermaquepts'),
          )
      ),
    ('Cryepts', (
            ('Calcicryepts', 'Calcicryepts'),
            ('Dystrocryepts', 'Dystrocryepts'),
            ('Haplocryepts', 'Haplocryepts'),
            ('Humicryepts', 'Humicryepts'),
          )
      ),
    ('Gelepts', (
            ('Dystrogelepts', 'Dystrogelepts'),
            ('Haplogelepts', 'Haplogelepts'),
            ('Humigelepts', 'Humigelepts'),
          )
      ),
    ('Udepts', (
            ('Durudepts', 'Durudepts'),
            ('Dystrudepts', 'Dystrudepts'),
            ('Eutrudepts', 'Eutrudepts'),
            ('Fragiudepts', 'Fragiudepts'),
            ('Humudepts', 'Humudepts'),
            ('Sulfudepts', 'Sulfudepts'),
          )
      ),
    ('Ustepts', (
            ('Calciustepts', 'Calciustepts'),
            ('Durustepts', 'Durustepts'),
            ('Dystrustepts', 'Dystrustepts'),
            ('Haplustepts', 'Haplustepts'),
            ('Humustepts', 'Humustepts'),
          )
      ),
    ('Xerepts', (
            ('Calcixerepts', 'Calcixerepts'),
            ('Durixerepts', 'Durixerepts'),
            ('Dystroxerepts', 'Dystroxerepts'),
            ('Fragixerepts', 'Fragixerepts'),
            ('Haploxerepts', 'Haploxerepts'),
            ('Humixerepts', 'Humixerepts'),
          )
      ),
#Andisols - Great Groups
    ('Aquands', (
            ('Cryaquands', 'Cryaquands'),
            ('Duraquands', 'Duraquands'),
            ('Endoaquands', 'Endoaquands'),
            ('Epiaquands', 'Epiaquands'),
            ('Gelaquands', 'Gelaquands'),
            ('Melanaquands', 'Melanaquands'),
            ('Placaquands', 'Placaquands'),
            ('Vitraquands', 'Vitraquands'),
          )
      ),
    ('Cryands', (
            ('Duricryands', 'Duricryands'),
            ('Fulvicryands', 'Fulvicryands'),
            ('Haplocryands', 'Haplocryands'),
            ('Hydrocryands', 'Hydrocryands'),
            ('Melanocryands', 'Melanocryands'),
            ('Vtiricryands', 'Vtiricryands'),
          )
      ),
    ('Gelands', (
            ('Vitrigelands', 'Vitrigelands'),
          )
      ),
    ('Torrands', (
            ('Durritorrands', 'Durritorrands'),
            ('Haplotorrands', 'Haplotorrands'),
            ('Vitritorrands', 'Vitritorrands'),
          )
      ),
    ('Udands', (
            ('Durudands', 'Durudands'),
            ('Fulvudands', 'Fulvudands'),
            ('Hapludands', 'Hapludands'),
            ('Hydrudands', 'Hydrudands'),
            ('Melanudands', 'Melanudands'),
            ('Placudands', 'Placudands'),
          )
      ),
    ('Ustands', (
            ('Durustands', 'Durustands'),
            ('Haplustands', 'Haplustands'),
          )
      ),
    ('Vitrands', (
            ('Udivitrands', 'Udivitrands'),
            ('Ustivitrands', 'Ustivitrands'),
          )
      ),
    ('Xerands', (
            ('Haploxerands', 'Haploxerands'),
            ('Melanoxerands', 'Melanoxerands'),
            ('Vitrixerands', 'Vitrixerands'),
          )
      ),
#Gelisols - Great Groups
    ('Histels', (
            ('Fibristels', 'Fibristels'),
            ('Folistels', 'Folistels'),
            ('Glacistels', 'Glacistels'),
            ('Hemistels', 'Hemistels'),
            ('Sapristels', 'Sapristels'),
          )
      ),
    ('Orthels', (
            ('Anhyorthels', 'Anhyorthels'),
            ('Aquorthels', 'Aquorthels'),
            ('Argiorthels', 'Argiorthels'),
            ('Haplorthels', 'Haplorthels'),
            ('Historthels', 'Historthels'),
            ('Mollorthels', 'Mollorthels'),
            ('Psammorthels', 'Psammorthels'),
            ('Umbrorthels', 'Umbrorthels'),
          )
      ),
    ('Turbels', (
            ('Anhyturbels', 'Anhyturbels'),
            ('Aquiturbels', 'Aquiturbels'),
            ('Haploturbels', 'Haploturbels'),
            ('Histoturbels', 'Histoturbels'),
            ('Molliturbels', 'Molliturbels'),
            ('Psammoturbels', 'Psammoturbels'),
            ('Umbriturbels', 'Umbriturbels'),
          )
      ),
#Histosols - Great Groups
    ('Fibrists', (
            ('Cryofibrists', 'Cryofibrists'),
            ('Haplofibrists', 'Haplofibrists'),
            ('Sphagnofibrists', 'Sphagnofibrists'),
          )
      ),
    ('Folists', (
            ('Cryofolists', 'Cryofolists'),
            ('Torrifolists', 'Torrifolists'),
            ('Udifolists', 'Udifolists'),
            ('Ustifolists', 'Ustifolists'),
          )
      ),
    ('Hemists', (
            ('Cryohemists', 'Cryohemists'),
            ('Haplohemists', 'Haplohemists'),
            ('Luvihemists', 'Luvihemists'),
            ('Sulfihemists', 'Sulfihemists'),
            ('Sulfohemists', 'Sulfohemists'),
          )
      ),
    ('Saprists', (
            ('Cryosaprists', 'Cryosaprists'),
            ('Haplosaprists', 'Haplosaprists'),
            ('Sulfisaprists', 'Sulfisaprists'),
            ('Sulfosaprists', 'Sulfosaprists'),
          )
      ),
    ('Wassists', (
            ('Frasiwassists', 'Frasiwassists'),
            ('Haplowassists', 'Haplowassists'),
            ('Sulfiwassists', 'Sulfiwassists'),
          )
      ),
#Aridisols - Great Groups
    ('Argids', (
            ('Calciargids', 'Calciargids'),
            ('Gypisargids', 'Gypisargids'),
            ('Haplargids', 'Haplargids'),
            ('Natrargids', 'Natrargids'),
            ('Paleargids', 'Paleargids'),
            ('Petroargids', 'Petroargids'),
          )
      ),
    ('Calcids', (
            ('Haplocalcids', 'Haplocalcids'),
            ('Petrocalcids', 'Petrocalcids'),
          )
      ),
    ('Cambids', (
            ('Aquicambids', 'Aquicambids'),
            ('Haplocambids', 'Haplocambids'),
            ('Petrocambids', 'Petrocambids'),
          )
      ),
    ('Cryids', (
            ('Argicryids', 'Argicryids'),
            ('Calcicryids', 'Calcicryids'),
            ('Gypsicryids', 'Gypsicryids'),
            ('Haplocryids', 'Haplocryids'),
            ('Petrocryids', 'Petrocryids'),
            ('Salicryids', 'Salicryids'),
          )
      ),
    ('Durids', (
            ('Argidurids', 'Argidurids'),
            ('Haplodurids', 'Haplodurids'),
            ('Natridurids', 'Natridurids'),
          )
      ),
    ('Gypsids', (
            ('Argigypsids', 'Argigypsids'),
            ('Calcigypsids', 'Calcigypsids'),
            ('Haplogypsids', 'Haplogypsids'),
            ('Natrigypsids', 'Natrigypsids'),
            ('Petrogypsids', 'Petrogypsids'),
          )
      ),
    ('Salids', (
            ('Aquisalids', 'Aquisalids'),
            ('Haplosalids', 'Haplosalids'),
          )
      ),
#Vertisols
    ('Aquerts', (
            ('Calciaquerts', 'Calciaquerts'),
            ('Duraquerts', 'Duraquerts'),
            ('Dystraquerts', 'Dystraquerts'),
            ('Endoaquerts', 'Endoaquerts'),
            ('Epiaquerts', 'Epiaquerts'),
            ('Natraquerts', 'Natraquerts'),
            ('Salaquerts', 'Salaquerts'),
            ('Sulfaquerts', 'Sulfaquerts'),
          )
      ),
    ('Cryerts', (
            ('Haplocryerts', 'Haplocryerts'),
            ('Humicryerts', 'Humicryerts'),
          )
      ),
    ('Torrerts', (
            ('Calcitorrerts', 'Calcitorrerts'),
            ('Gypsitorrerts', 'Gypsitorrerts'),
            ('Haplotorrerts', 'Haplotorrerts'),
            ('Salitorrerts', 'Salitorrerts'),
          )
      ),
    ('Uderts', (
            ('Dystruderts', 'Dystruderts'),
            ('Hapluderts', 'Hapluderts'),
          )
      ),
    ('Usterts', (
            ('Calciusterts', 'Calciusterts'),
            ('Dystrusterts', 'Dystrusterts'),
            ('Gypsiusterts', 'Gypsiusterts'),
            ('Haplusterts', 'Haplusterts'),
            ('Salusterts', 'Salusterts'),
          )
      ),
    ('Xererts', (
            ('Calcixererts', 'Calcixererts'),
            ('Durixererts', 'Durixererts'),
            ('Haploxererts', 'Haploxererts'),
          )
      ),
#Mollisols - Great Groups
    ('Albolls', (
            ('Argialbolls', 'Argialbolls'),
            ('Natralbolls', 'Natralbolls'),
          )
      ),
    ('Aquolls', (
            ('Argiaquolls', 'Argiaquolls'),
            ('Calciaquolls', 'Calciaquolls'),
            ('Cryaquolls', 'Cryaquolls'),
            ('Duraquolls', 'Duraquolls'),
            ('Endoaquolls', 'Endoaquolls'),
            ('Epiaquolls', 'Epiaquolls'),
            ('Natraquolls', 'Natraquolls'),
          )
      ),
    ('Cryolls', (
            ('Argicryolls', 'Argicryolls'),
            ('Calcicryolls', 'Calcicryolls'),
            ('Duricryolls', 'Duricryolls'),
            ('Haplocryolls', 'Haplocryolls'),
            ('Natricryolls', 'Natricryolls'),
            ('Palecryolls', 'Palecryolls'),
          )
      ),
    ('Gelolls', (
            ('Haplogelolls', 'Haplogelolls'),
          )
      ),
    ('Rendolls', (
            ('Cryrendolls', 'Cryrendolls'),
            ('Haprendolls', 'Haprendolls'),
          )
      ),
    ('Udolls', (
            ('Argiudolls', 'Argiudolls'),
            ('Calciudolls', 'Calciudolls'),
            ('Hapludolls', 'Hapludolls'),
            ('Natrudolls', 'Natrudolls'),
            ('Paleudolls', 'Paleudolls'),
            ('Vermudolls', 'Vermudolls'),
          )
      ),
    ('Ustolls', (
            ('Argiustolls', 'Argiustolls'),
            ('Calciustolls', 'Calciustolls'),
            ('Durustolls', 'Durustolls'),
            ('Haplustolls', 'Haplustolls'),
            ('Natrustolls', 'Natrustolls'),
            ('Paleustolls', 'Paleustolls'),
            ('Vermustolls', 'Vermustolls'),
          )
      ),
    ('Xerolls', (
            ('Argixerolls', 'Argixerolls'),
            ('Calcixerolls', 'Calcixerolls'),
            ('Durixerolls', 'Durixerolls'),
            ('Haploxerolls', 'Haploxerolls'),
            ('Natrixerolls', 'Natrixerolls'),
            ('Palexerolls', 'Palexerolls'),
          )
      ),
# Alfisols - Great Groups
    ('Aqualfs', (
            ('Albaqualfs', 'Albaqualfs'),
            ('Cryaqualfs', 'Cryaqualfs'),
            ('Duraqualfs', 'Duraqualfs'),
            ('Endoaqualfs', 'Endoaqualfs'),
            ('Epiaqualfs', 'Epiaqualfs'),
            ('Fragiaqualfs', 'Fragiaqualfs'),
            ('Glossaqualfs', 'Glossaqualfs'),
            ('Kandiaqualfs', 'Kandiaqualfs'),
            ('Natraqualfs', 'Natraqualfs'),
            ('Plinthaqualfs', 'Plinthaqualfs'),
            ('Vermaqualfs', 'Vermaqualfs'),
          )
      ),
    ('Cryalfs', (
            ('Glossocryalfs', 'Glossocryalfs'),
            ('Haplocryalfs', 'Haplocryalfs'),
            ('Palecryalfs', 'Palecryalfs'),
          )
      ),
    ('Udalfs', (
            ('Ferrudalfs', 'Ferrudalfs'),
            ('Fragiudalfs', 'Fragiudalfs'),
            ('Fraglossudalfs', 'Fraglossudalfs'),
            ('Glossudalfs', 'Glossudalfs'),
            ('Hapludalfs', 'Hapludalfs'),
            ('Kandiudalfs', 'Kandiudalfs'),
            ('Kanhapludalfs', 'Kanhapludalfs'),
            ('Natrustalfs', 'Natrustalfs'),
            ('Paleudalfs', 'Paleudalfs'),
            ('Rhodudalfs', 'Rhodudalfs'),
          )
      ),
    ('Ustalfs', (
            ('Durustalfs', 'Durustalfs'),
            ('Haplustalfs', 'Haplustalfs'),
            ('Kandiustalfs', 'Kandiustalfs'),
            ('Kanhaplustalfs', 'Kanhaplustalfs'),
            ('Natrustalfs', 'Natrustalfs'),
            ('Paleustalfs', 'Paleustalfs'),
            ('Plinthustalfs', 'Plinthustalfs'),
            ('Rhodustalfs', 'Rhodustalfs'),
          )
      ),
    ('Xeralfs', (
            ('Durixeralfs', 'Durixeralfs'),
            ('Fragixeralfs', 'Fragixeralfs'),
            ('Haploxeralfs', 'Haploxeralfs'),
            ('Natrixeralfs', 'Natrixeralfs'),
            ('Palexeralfs', 'Palexeralfs'),
            ('Plinthoxeralfs', 'Plinthoxeralfs'),
            ('Rhodoxeralfs', 'Rhodoxeralfs'),
          )
      ),
#Spodosols - Great Groups
    ('Aquods', (
            ('Alaquods', 'Alaquods'),
            ('Cryaquods', 'Cryaquods'),
            ('Duraquods', 'Duraquods'),
            ('Endoaquods', 'Endoaquods'),
            ('Epiaquods', 'Epiaquods'),
            ('Fragiaquods', 'Fragiaquods'),
            ('Placaquods', 'Placaquods'),
          )
      ),
    ('Cryods', (
            ('Duricryods', 'Duricryods'),
            ('Haplocryods', 'Haplocryods'),
            ('Humicryods', 'Humicryods'),
            ('Placocryods', 'Placocryods'),
          )
      ),
    ('Gelods', (
            ('Haplogelods', 'Haplogelods'),
            ('Humigelods', 'Humigelods'),
          )
      ),
    ('Humods', (
            ('Durihumods', 'Durihumods'),
            ('Fragihumods', 'Fragihumods'),
            ('Haplohumods', 'Haplohumods'),
            ('Placohumods', 'Placohumods'),
          )
      ),
    ('Orthods', (
            ('Alorthods', 'Alorthods'),
            ('Durorthods', 'Durorthods'),
            ('Fragiorthods', 'Fragiorthods'),
            ('Haplorthods', 'Haplorthods'),
            ('Placorthods', 'Placorthods'),
          )
      ),
#Ultisols
    ('Aquults', (
            ('Albaquults', 'Albaquults'),
            ('Endoaquults', 'Endoaquults'),
            ('Epiaquults', 'Epiaquults'),
            ('Fragiaquults', 'Fragiaquults'),
            ('Kandiaquults', 'Kandiaquults'),
            ('Kanhaplaquults', 'Kanhaplaquults'),
            ('Paleaquults', 'Paleaquults'),
            ('Plinthaquults', 'Plinthaquults'),
            ('Umbraquults', 'Umbraquults'),
          )
      ),
    ('Humults', (
            ('Haplohumults', 'Haplohumults'),
            ('Kandihumults', 'Kandihumults'),
            ('Kanhaplohumults', 'Kanhaplohumults'),
            ('Palehumults', 'Palehumults'),
            ('Plinthohumults', 'Plinthohumults'),
            ('Sombrihumults', 'Sombrihumults'),
          )
      ),
    ('Udults', (
            ('Fragiudults', 'Fragiudults'),
            ('Hapludults', 'Hapludults'),
            ('Kandiudults', 'Kandiudults'),
            ('Kanhapludults', 'Kanhapludults'),
            ('Paleudults', 'Paleudults'),
            ('Plinthudults', 'Plinthudults'),
            ('Rhodudults', 'Rhodudults'),
          )
      ),
    ('Ustults', (
            ('Haplustults', 'Haplustults'),
            ('Kandiustults', 'Kandiustults'),
            ('Kanhaplustults', 'Kanhaplustults'),
            ('Paleustults', 'Paleustults'),
            ('Plinthustults', 'Plinthustults'),
            ('Rhodustults', 'Rhodustults'),
          )
      ),
    ('Xerults', (
            ('Haploxerults', 'Haploxerults'),
            ('Palexerults', 'Palexerults'),
          )
      ),
#Oxisols
    ('Aquox', (
            ('Acraquox', 'Acraquox'),
            ('Eutraquox', 'Eutraquox'),
            ('Haplaxquox', 'Haplaxquox'),
            ('Plinthaquox', 'Plinthaquox'),
          )
      ),
    ('Perox', (
            ('Acroperox', 'Acroperox'),
            ('Eutroperox', 'Eutroperox'),
            ('Haploperox', 'Haploperox'),
            ('Kandiperox', 'Kandiperox'),
            ('Sombriperox', 'Sombriperox'),
          )
      ),
    ('Torrox', (
            ('Acrotorrox', 'Acrotorrox'),
            ('Eutrotorrox', 'Eutrotorrox'),
            ('Haplotorrox', 'Haplotorrox'),
          )
      ),
    ('Udox', (
            ('Acrudox', 'Acrudox'),
            ('Eutrudox', 'Eutrudox'),
            ('Hapludox', 'Hapludox'),
            ('Kandiudox', 'Kandiudox'),
            ('Sombriudox', 'Sombriudox'),
          )
      ),
    ('Ustox', (
            ('Acrustox', 'Acrustox'),
            ('Eutrustox', 'Eutrustox'),
            ('Haplustox', 'Haplustox'),
            ('Kandiustox', 'Kandiustox'),
            ('Sambriustox', 'Sambriustox'),
          )
      ),
      )

    suborder = models.ForeignKey('SubOrders')
    greatgroup = models.CharField(max_length=50,choices=great_groups, unique=True)


    def __str__(self):
               # __unicode__ on Python 2
        return self.greatgroup

#     ('zzzzzzzzzzzzz', (
#             ('zzzzzzzzzzzzz', 'zzzzzzzzzzzzz'),
#             ('zzzzzzzzzzzzz', 'zzzzzzzzzzzzz'),
#             ('zzzzzzzzzzzzz', 'zzzzzzzzzzzzz'),
#             ('zzzzzzzzzzzzz', 'zzzzzzzzzzzzz'),
#             ('zzzzzzzzzzzzz', 'zzzzzzzzzzzzz'),
#             ('zzzzzzzzzzzzz', 'zzzzzzzzzzzzz'),
#           )
#       ),
# ## GREATGROUP FORMATIVE ELEMENTS ##
# Acr	        Extreme weathering
# Al	        low iron
# Alb		    An albic horizon
# Anhy		Very dry
# Anthr		An anthropic epipedon
# Aqu		    Aquic condition
# Argi	    Presence of an argillic horizon
# Calci,calc 	A calcic horizon
# Cry	        Cold
# Dur	        A duripan
# Dystr,dyst 	Low base saturation
# Endo		Implying a ground water table
# Epi		    Implying a perched water table
# Eutr		High base saturation
# Ferr		Presence of iron
# Fibr	    Least decomposed stage
# Fluv		Flood plain
# Fol		    Mass of leaves
# Fragi		Presence of fragipan
# Fragloss	See the formative elements "frag" and "gloss"
# Fulv	    Dark brown color, presence of organic carbon
# Glac	    Glacier	Ice lenses or wedges
# Gyps	    Presence of gypsic horizon
# Gloss	    Presence of a glossic horizon
# Hal		    Salty
# Hapl	    Minimum horizon development
# Hem		    Intermediate stage of decomposition
# Hist	    Presence of organic materials
# Hum	        Presence of organic matter
# Hydr        Presence of water
# Kand, kan   1:1 layer silicate clays
# Luv	        Illuvial
# Melan	    Black, presence of organic carbon
# Moll	    Presence of a mollic epipedon
# Natr	    Presence of natric horizon
# Pale	    Excessive development
# Petr	    A cemented horizon
# Plac        Presence of thin pan
# Plagg	    Presence of plaggen epipedon
# Plinth	    Presence of plinthite
# Psamm	    Sandy texture
# Quartz	    High quartz content
# Rhod	    Dark red color
# Sal	        Presence of salic horizon
# Sapr	    Most decomposed stage
# Somb	    Presence of sombric horizon
# Sphagn	    Presence of Sphagnum
# Sulf	    Presence of sulfides or their oxidation products
# Torr	    Torric moisture regime
# Ud	        Udic moisture regime
# Umbr	    Presence of umbric epipedon
# Ust		    Ustic moisture regime
# Verm		Wormy, or mixed by animals
# Vitr		Presence of glass
# Xer		    Xeric moisture regime
