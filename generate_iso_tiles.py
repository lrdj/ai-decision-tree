#!/usr/bin/env python3
"""
Generate an isometric map of decision steps as SVG tiles.
Each step is rendered as an isometric diamond (top face) with a label.
Usage: python3 generate_iso_tiles.py > iso_map.svg
"""
import math
import sys

# Define your decision steps and their grid positions (i, j)
steps = [
    ("1: Org & Business Readiness", (0, 0)),
    ("2: Compliance & Security",    (1, 0)),
    ("3: Known & Pred. Qs",         (2, 0)),
    ("4: Harm & Off-limits",       (3, 0)),
    ("5: Tone & Persona",          (4, 0)),
    ("6: Multi-step/Stateful",      (5, 0)),
    ("7: Human-in-Loop",            (6, 0)),
    ("8: Pilot & CI",               (7, 0)),
]

# Tile size (edge length) and isometric projection params
L = 100.0  # nominal tile edge length
cos30 = math.cos(math.radians(30))
sin30 = math.sin(math.radians(30))
dx = L * cos30
dy = L * sin30

# SVG canvas setup
margin = 50
width = int((len(steps) + 1) * dx + 2 * margin)
height = int(len(steps) * dy + L + 2 * margin)
print('<?xml version="1.0" encoding="UTF-8"?>')
print(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">')
# Define arrow marker for later use
print('  <defs>')
print('    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">')
print('      <path d="M0,0 L0,6 L9,3 Z" fill="#004d40"/>')
print('    </marker>')
print('  </defs>')

def iso_coords(i, j):
    """Convert grid coords (i, j) to 2D isometric coords."""
    x0 = margin + (i - j) * dx + len(steps) * dx / 2
    y0 = margin + (i + j) * dy
    return x0, y0

def draw_tile(x, y, label):
    # Top face diamond pts: A, B, C, D
    A = (x,         y)
    B = (x + dx,    y - dy)
    C = (x,         y - 2*dy)
    D = (x - dx,    y - dy)
    # Draw polygon for top face
    pts = ' '.join(f'{px:.2f},{py:.2f}' for px, py in (A, B, C, D))
    print(f'  <polygon points="{pts}" fill="#e0f7fa" stroke="#006064" stroke-width="2"/>')
    # Add label text at center top-ish
    tx = x
    ty = y - dy - 5
    # Escape label for XML
    label_esc = label.replace('&', '&amp;')
    print(f'  <text x="{tx:.2f}" y="{ty:.2f}" text-anchor="middle" ' +
          'font-family="sans-serif" font-size="12" fill="#004d40">')
    print(f'    {label_esc}')
    print('  </text>')

  # Draw all tiles and connecting arrows
for idx, (label, (i, j)) in enumerate(steps):
    x, y = iso_coords(i, j)
    draw_tile(x, y, label)
    # Draw arrow to next tile
    if idx < len(steps) - 1:
        nx, ny = iso_coords(*steps[idx + 1][1])
        # arrow from east of current to west of next
        ax = x + dx * 0.5
        ay = y - dy * 0.5
        bx = nx - dx * 0.5
        by = ny - dy * 0.5
        print(f'  <line x1="{ax:.2f}" y1="{ay:.2f}" x2="{bx:.2f}" y2="{by:.2f}" ' +
              'stroke="#004d40" stroke-width="2" marker-end="url(#arrow)"/>')

print('</svg>')