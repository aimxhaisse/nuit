# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

@live()
def setup():
    bpm.set(115)

    tracks.setup({
        'hh': tracks.mk_sampler(fxs={
            'hpf': fx.mk_hpf(cutoff=0.7, resonance=0.0),
        })
    })

sp = sampler.new('drumnibus')
mode = 0

def hh_exploration_0(flavor, params):
    patterns = [
        '1...1...2..1....',
        '.001.001.001..1.',
        '..3...3...3...3.',
    ]

    samples = {
        '0': {'sp': 'oh-draconisd921', 'args': {'end': 0.03}},
        '1': {'sp': 'oh-draconisd921', 'args': {'end': 0.13}},
        '2': {'sp': 'oh-draconisd922', 'args': {'end': 0.14, 'rate': 0.957}},
        '3': {'sp': 'oh-draconisd922', 'args': {'start': 0.13, 'end': 0.3, 'rate': 0.957}},
    }
    
    for i in range(16):
        c = patterns[flavor][i]
        if c in samples:
            p = samples[c]['args'] | params
            sp.play(samples[c]['sp'], **p)
        sp.play('oh')
        sleep(1/4)


@loop('hh', beats=4)
def hh_explorations():
    match mode:
        case 0:
            hh_exploration_0(2, {'pan': 0.3})
