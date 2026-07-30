#!/usr/bin/env python3
"""Add short descriptions to Jekyll post front matter.

Run from the repository root after filling the DESCRIPTIONS mapping. The
script is intentionally conservative: it only inserts `description` when the
field is missing and preserves the remainder of each post verbatim.
"""
from pathlib import Path

DESCRIPTIONS = {
    "2026-05-28-ciclo-criado-pela-ia.md": "Como o ganho de produtividade com IA pode aumentar o ritmo e a densidade do trabalho sem reduzir a carga percebida.",
    "2026-06-26-wellhub.md": "Exemplos de consultas e endpoints usados para realizar check-ins no Wellhub.",
    "2026-06-29-pr-visual.md": "Procedimentos para adicionar evidências visuais a pull requests sem versionar arquivos binários.",
    "2026-07-04-assistento-skill.md": "Uma skill pessoal para padronizar diagramas, tarefas, planos e fluxos de trabalho com agentes.",
    "2026-07-23-agents-oficiais-criacao.md": "Boas práticas oficiais para criar arquivos AGENTS.md úteis para agentes de IA.",
    "2026-07-23-como-criar-agents.md": "Estrutura recomendada e exemplos reais para orientar agentes de IA em repositórios.",
    "2026-07-23-repos-ia-github-trending.md": "Curadoria de projetos de IA em destaque no GitHub, com foco em agentes, contexto e dados.",
    "2026-07-23-self-host-ia-coolify-agentes-rag.md": "Ferramentas open source para hospedar aplicações, agentes, RAG e serviços de IA por conta própria.",
    "2026-07-23-trilhas-cursos-ia.md": "Cursos e trilhas para aprender IA, prompt engineering, agentes, automação e APIs.",
    "2026-07-23-turbovec-turboquant.md": "Referências sobre o índice vetorial Rust Turbovec e a compressão de embeddings com TurboQuant.",
    "2026-07-24-colibri-motor-local-ia.md": "Como o Colibri usa streaming seletivo para executar modelos MoE grandes em hardware comum.",
    "2026-07-24-ferramentas-claude-avancadas.md": "Ferramentas para ampliar o Claude com APIs, grafos de conhecimento e skills especializadas.",
    "2026-07-25-ferramentas-ia-open-source.md": "Seleção de ferramentas open source para automação, reuniões e segurança com IA.",
    "2026-07-25-omniroute-gateway-ia.md": "Gateway open source que unifica provedores de IA, oferece fallback e ajuda a reduzir custos de tokens.",
    "2026-07-26-agentes-ia-pesquisa-automacao.md": "Agentes para pesquisa profunda na web e automação de fluxos complexos em navegadores.",
    "2026-07-26-ferramentas-plugins-skills-claude.md": "Visão geral de MCPs, skills, plugins e conectores para estender o Claude.",
    "2026-07-26-hermes-agente-ia-open-source.md": "Recursos e referências do Hermes, agente open source com memória, skills e ferramentas.",
    "2026-07-26-melhores-ferramentas-ia-2026.md": "Panorama de ferramentas de IA para pesquisa, criação, programação, design e automação em 2026.",
    "2026-07-26-youtube-prompts-estrategia-canal.md": "Prompts e especialistas de IA para planejar, produzir, otimizar e monetizar canais no YouTube.",
    "2026-07-27-ai-skills.md": "Framework com dez competências de IA, de prompt engineering a gestão de LLMs, com guias práticos.",
    "2026-07-27-markitdown-documentos-markdown.md": "Como converter documentos em Markdown com MarkItDown para economizar tokens e preparar dados para LLMs.",
    "2026-07-27-sites-de-empregos-remotos.md": "Curadoria de plataformas e referências para encontrar oportunidades de trabalho remoto.",
    "2026-07-29-crawlee-web-scraping.md": "Bibliotecas, técnicas e cuidados para coletar dados da web e preparar datasets para IA.",
    "2026-07-29-design-md-sistemas-design-ia.md": "Como usar DESIGN.md para fornecer referências e tokens de design consistentes a agentes de IA.",
    "2026-07-29-hyper-research-deep-research-agent.md": "Um pipeline open source para pesquisa profunda com verificação, proveniência e memória persistente.",
    "2026-07-29-kilo-code-agentes-ia.md": "O Kilo Code combina agentes de codificação open source, múltiplos modelos e soberania técnica.",
    "2026-07-29-kimi-k3-local.md": "Requisitos e quantizações dinâmicas para executar o Kimi K3 localmente com Unsloth.",
    "2026-07-29-mantis-security-review.md": "Como agentes especializados podem analisar, reproduzir e corrigir vulnerabilidades de software.",
    "2026-07-29-open-code-review.md": "Revisão de código com uma arquitetura híbrida que combina regras determinísticas e agentes LLM.",
    "2026-07-29-openviking-context-database-ai-agents.md": "Um banco de contexto com hierarquia de sistema de arquivos para memória e recuperação de agentes.",
    "2026-07-30-agentic-awesome-skills.md": "Biblioteca instalável de skills reutilizáveis para Claude Code, Cursor e Gemini CLI.",
    "2026-07-30-arvore-modelos-claude.md": "Guia visual para escolher entre modelos Claude conforme velocidade, complexidade e custo.",
    "2026-07-30-langgraph-10-motivos.md": "Dez motivos técnicos para usar LangGraph na construção de agentes com estado e execução durável.",
    "2026-07-30-llmfit-otimizar-hardware.md": "Ferramenta que identifica quais modelos locais melhor combinam com o hardware disponível.",
    "2026-07-30-pxpipe-corte-tokens-imagens.md": "Como renderizar contexto como imagem pode reduzir tokens de entrada e custos em fluxos multimodais.",
    "2026-07-30-swe-skills-bench-utilidade-real-skills-agentes.md": "Resultados de benchmarks que medem quando skills realmente ajudam agentes em tarefas de software.",
    "2026-07-30-unsloth-treinamento-local-modelos.md": "Como usar Unsloth para treinar e executar modelos de IA localmente com menos memória.",
}

for path in sorted(Path("_posts").glob("*.md")):
    description = DESCRIPTIONS.get(path.name)
    if not description:
        raise SystemExit(f"Missing description for {path.name}")
    text = path.read_text()
    if "\ndescription:" in text.split("---", 2)[1]:
        continue
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise SystemExit(f"Invalid front matter in {path}")
    frontmatter, body = parts[1], parts[2]
    path.write_text(f"---{frontmatter.rstrip()}\ndescription: {description!r}\n---{body}")
