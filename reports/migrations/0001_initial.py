# Generated by Django 3.0.8 on 2020-07-18 17:50

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('sec_cover', models.IntegerField(choices=[(0, 'cover'), (1, 'title'), (2, 'none')], default=0, verbose_name='Cover')),
                ('sec_toc', models.BooleanField(default=True, verbose_name='Table of Contents')),
                ('sec_es', models.BooleanField(default=True, verbose_name='Executive Summary')),
                ('sec_sor', models.BooleanField(default=True, verbose_name='Summary of Results')),
                ('sec_method', models.BooleanField(default=True, verbose_name='Methodology')),
                ('sec_find', models.BooleanField(default=True, verbose_name='Findings')),
                ('sec_find_desc', models.BooleanField(default=True, verbose_name='Description')),
                ('sec_find_evid', models.BooleanField(default=True, verbose_name='Evidence')),
                ('sec_find_sol', models.BooleanField(default=True, verbose_name='Solution')),
                ('sec_conc', models.BooleanField(default=True, verbose_name='Conclusion')),
                ('cover_title', models.CharField(blank=True, max_length=50, verbose_name='Title')),
                ('cover_company_name', models.CharField(blank=True, max_length=50, verbose_name='Company Name')),
                ('cover_contact_name', models.CharField(blank=True, max_length=50, verbose_name='Contact Name')),
                ('cover_contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Contact Email Address')),
                ('cover_contact_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Contact Phone Number')),
                ('es_text', models.TextField(blank=True, verbose_name='Executive Summary Text')),
                ('method_text', models.TextField(blank=True, verbose_name='Methodology Text')),
                ('conc_text', models.TextField(blank=True, verbose_name='Conclusion Text')),
                ('title_font', models.CharField(default='Droid Serif', max_length=50)),
                ('title_size', models.IntegerField(default=26)),
                ('title_bold', models.BooleanField(default=True)),
                ('title_italic', models.BooleanField(default=False)),
                ('title_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=37)),
                ('heading_1_font', models.CharField(default='Droid Serif', max_length=50)),
                ('heading_1_size', models.IntegerField(default=16)),
                ('heading_1_bold', models.BooleanField(default=True)),
                ('heading_1_italic', models.BooleanField(default=False)),
                ('heading_1_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=37)),
                ('heading_2_font', models.CharField(default='Droid Serif', max_length=50)),
                ('heading_2_size', models.IntegerField(default=14)),
                ('heading_2_bold', models.BooleanField(default=True)),
                ('heading_2_italic', models.BooleanField(default=False)),
                ('heading_2_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=37)),
                ('heading_3_font', models.CharField(default='Droid Serif', max_length=50)),
                ('heading_3_size', models.IntegerField(default=14)),
                ('heading_3_bold', models.BooleanField(default=True)),
                ('heading_3_italic', models.BooleanField(default=False)),
                ('heading_3_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=37)),
                ('normal_font', models.CharField(default='Roboto', max_length=50)),
                ('normal_size', models.IntegerField(default=12)),
                ('normal_bold', models.BooleanField(default=False)),
                ('normal_italic', models.BooleanField(default=False)),
                ('normal_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=7)),
                ('caption_font', models.CharField(default='Roboto', max_length=50)),
                ('caption_size', models.IntegerField(default=11)),
                ('caption_bold', models.BooleanField(default=False)),
                ('caption_italic', models.BooleanField(default=True)),
                ('caption_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=7)),
                ('risk_critical_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=45, verbose_name='Critical Color')),
                ('risk_high_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=30, verbose_name='High Color')),
                ('risk_medium_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=51, verbose_name='Medium Color')),
                ('risk_low_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=126, verbose_name='Low Color')),
                ('risk_info_color', models.IntegerField(choices=[(0, 'aliceblue'), (1, 'antiquewhite'), (2, 'aqua'), (3, 'aquamarine'), (4, 'azure'), (5, 'beige'), (6, 'bisque'), (7, 'black'), (8, 'blanchedalmond'), (9, 'blue'), (10, 'blueviolet'), (11, 'brown'), (12, 'burlywood'), (13, 'cadetblue'), (14, 'chartreuse'), (15, 'chocolate'), (16, 'coral'), (17, 'cornflowerblue'), (18, 'cornsilk'), (19, 'crimson'), (20, 'cyan'), (21, 'darkblue'), (22, 'darkcyan'), (23, 'darkgoldenrod'), (24, 'darkgray'), (25, 'darkgreen'), (26, 'darkgrey'), (27, 'darkkhaki'), (28, 'darkmagenta'), (29, 'darkolivegreen'), (30, 'darkorange'), (31, 'darkorchid'), (32, 'darkred'), (33, 'darksalmon'), (34, 'darkseagreen'), (35, 'darkslateblue'), (36, 'darkslategray'), (37, 'darkslategrey'), (38, 'darkturquoise'), (39, 'darkviolet'), (40, 'deeppink'), (41, 'deepskyblue'), (42, 'dimgray'), (43, 'dimgrey'), (44, 'dodgerblue'), (45, 'firebrick'), (46, 'floralwhite'), (47, 'forestgreen'), (48, 'fuchsia'), (49, 'gainsboro'), (50, 'ghostwhite'), (51, 'gold'), (52, 'goldenrod'), (53, 'gray'), (54, 'green'), (55, 'greenyellow'), (56, 'grey'), (57, 'honeydew'), (58, 'hotpink'), (59, 'indianred'), (60, 'indigo'), (61, 'ivory'), (62, 'khaki'), (63, 'lavender'), (64, 'lavenderblush'), (65, 'lawngreen'), (66, 'lemonchiffon'), (67, 'lightblue'), (68, 'lightcoral'), (69, 'lightcyan'), (70, 'lightgoldenrodyellow'), (71, 'lightgray'), (72, 'lightgreen'), (73, 'lightgrey'), (74, 'lightpink'), (75, 'lightsalmon'), (76, 'lightseagreen'), (77, 'lightskyblue'), (78, 'lightslategray'), (79, 'lightslategrey'), (80, 'lightsteelblue'), (81, 'lightyellow'), (82, 'lime'), (83, 'limegreen'), (84, 'linen'), (85, 'magenta'), (86, 'maroon'), (87, 'mediumaquamarine'), (88, 'mediumblue'), (89, 'mediumorchid'), (90, 'mediumpurple'), (91, 'mediumseagreen'), (92, 'mediumslateblue'), (93, 'mediumspringgreen'), (94, 'mediumturquoise'), (95, 'mediumvioletred'), (96, 'midnightblue'), (97, 'mintcream'), (98, 'mistyrose'), (99, 'moccasin'), (100, 'navajowhite'), (101, 'navy'), (102, 'oldlace'), (103, 'olive'), (104, 'olivedrab'), (105, 'orange'), (106, 'orangered'), (107, 'orchid'), (108, 'palegoldenrod'), (109, 'palegreen'), (110, 'paleturquoise'), (111, 'palevioletred'), (112, 'papayawhip'), (113, 'peachpuff'), (114, 'peru'), (115, 'pink'), (116, 'plum'), (117, 'powderblue'), (118, 'purple'), (119, 'rebeccapurple'), (120, 'red'), (121, 'rosybrown'), (122, 'royalblue'), (123, 'saddlebrown'), (124, 'salmon'), (125, 'sandybrown'), (126, 'seagreen'), (127, 'seashell'), (128, 'sienna'), (129, 'silver'), (130, 'skyblue'), (131, 'slateblue'), (132, 'slategray'), (133, 'slategrey'), (134, 'snow'), (135, 'springgreen'), (136, 'steelblue'), (137, 'tan'), (138, 'teal'), (139, 'thistle'), (140, 'tomato'), (141, 'turquoise'), (142, 'violet'), (143, 'wheat'), (144, 'white'), (145, 'whitesmoke'), (146, 'yellow'), (147, 'yellowgreen')], default=41, verbose_name='Info Color')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('media', models.FileField(max_length=256, upload_to='reports/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('proj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Proj')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
