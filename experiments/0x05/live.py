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
flavor = 0

def hh_exploration_0():
    patterns = [
        '1...2....3..1...',
    ]

    samples = {
        '1': {
            'sp': 'oh-draconisd921',
            'args': {'end': 0.13}
        },
        '2': {
            'sp': 'oh-draconisd922',
            'args': {'end': 0.07, 'rate': 0.96}
        },
        '3': {
            'sp': 'oh-draconisd922',
            'args': {'end': 0.25, 'rate': 0.96}
        }
    }
    
    for i in range(16):
        c = patterns[flavor][i]
        if c in samples:
            sp.play(samples[c]['sp'], **samples[c]['args'])
        sp.play('oh')
        sleep(1/4)


@loop('hh', beats=4)
def hh_explorations():
    match mode:
        case 0:
            hh_exploration_0()
