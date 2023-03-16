# Generated by Django 3.2.18 on 2023-03-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0098_pdf_epub_opt_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalproject",
            name="conf_py_file",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Path from project root to your Sphinx configuration file, typically named <code>conf.py</code>. Leave blank if you want us to find it for you.",
                max_length=255,
                verbose_name="Sphinx configuration file",
            ),
        ),
        migrations.AlterField(
            model_name="historicalproject",
            name="documentation_type",
            field=models.CharField(
                choices=[
                    ("sphinx", "Sphinx Html"),
                    ("mkdocs", "Mkdocs"),
                    ("sphinx_htmldir", "Sphinx HtmlDir"),
                    ("sphinx_singlehtml", "Sphinx Single Page HTML"),
                ],
                default="sphinx",
                help_text='Specify the type of documentation you are building. This will make the automatic Read the Docs builder detect your MkDocs or Sphinx configuration and build your project running Read the Docs\' default command. Using a readthedocs.yaml <a href="https://docs.readthedocs.io/en/stable/config-file/index.html">configuration file</a> allows you to change defaults or build documentation for <strong>other tools than Sphinx and MkDocs</strong>.',
                max_length=20,
                verbose_name="Documentation type",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="conf_py_file",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Path from project root to your Sphinx configuration file, typically named <code>conf.py</code>. Leave blank if you want us to find it for you.",
                max_length=255,
                verbose_name="Sphinx configuration file",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="documentation_type",
            field=models.CharField(
                choices=[
                    ("sphinx", "Sphinx Html"),
                    ("mkdocs", "Mkdocs"),
                    ("sphinx_htmldir", "Sphinx HtmlDir"),
                    ("sphinx_singlehtml", "Sphinx Single Page HTML"),
                ],
                default="sphinx",
                help_text='Specify the type of documentation you are building. This will make the automatic Read the Docs builder detect your MkDocs or Sphinx configuration and build your project running Read the Docs\' default command. Using a readthedocs.yaml <a href="https://docs.readthedocs.io/en/stable/config-file/index.html">configuration file</a> allows you to change defaults or build documentation for <strong>other tools than Sphinx and MkDocs</strong>.',
                max_length=20,
                verbose_name="Documentation type",
            ),
        ),
    ]
