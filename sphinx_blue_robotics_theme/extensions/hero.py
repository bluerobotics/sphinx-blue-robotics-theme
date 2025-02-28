from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class hero(nodes.General, nodes.Element):
    pass

def visit_hero_node(self, node):
    title = node.get('title', '')
    description = node.get('description', '')
    is_landing = node.get('is_landing', False)
    title_level = node.get('title_level', 'h1')
    bg_image = node.get('bg_image', '')

    if bg_image:
        bg_image = f'/{self.builder.config.html_static_path[0]}/{bg_image.lstrip("/")}'

    hero_class = 'br-hero br-hero-landing' if is_landing else 'br-hero'
    bg_style = f' style="background-image: url({bg_image})"' if bg_image else ''
    self.body.append(f'<div class="{hero_class}"{bg_style}>')
    self.body.append('<div class="br-hero-container">')
    
    if title:
        self.body.append(f'<{title_level} class="br-hero-title">{title}</{title_level}>')
    
    if description:
        self.body.append(f'<p class="br-hero-description">{description}</p>')
    
    self.body.append('</div>')
    self.body.append('</div>')

def depart_hero_node(self, node):
    pass

class HeroDirective(SphinxDirective):
    has_content = True
    option_spec = {
        'title': directives.unchanged,
        'description': directives.unchanged,
        'landing': directives.flag,
        'title-level': directives.unchanged,
        'bg-image': directives.unchanged,
    }

    def run(self):
        node = hero()
        
        node['title'] = self.options.get('title', '')
        node['description'] = self.options.get('description', '')
        node['is_landing'] = 'landing' in self.options
        node['bg_image'] = self.options.get('bg-image', '')
        
        title_level = self.options.get('title-level', 'h1')
        if title_level not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            raise ValueError('title-level must be one of: h1, h2, h3, h4, h5, h6')
        node['title_level'] = title_level
        return [node]

def setup(app):
    app.add_node(hero,
                 html=(visit_hero_node, depart_hero_node))
    app.add_directive('hero', HeroDirective)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }