# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

@live()
def setup():
    bpm.set(120)

    ctrls.mk_lfo('[x0]', rate=0.0125, intensity=0.25)

    tracks.setup({
        'mobylette': tracks.mk_sampler(fxs={
            'hpf': fx.mk_hpf(cutoff=ctrl('[x0]'), resonance=0),
            'chr': fx.mk_chorus(),
            'rev': fx.mk_reverb(time=0.4),
        }),
        'beats': tracks.mk_sampler(),
    })

    
sp1 = sampler.new('mxs-sample-db')
sp2 = sampler.new('elektron-2323')


@loop('mobylette', beats=4)
def pads():
    kit = sampler.Kit(sp1)

    return

    def get_rate():
        r = [1.5, 2.0, 4.0]
        rate = r[int(rnd.between(0, len(r)))]
        if rnd.one_in(2):
            rate = -rate
        return rate

    kit.set('a', lambda: {'name': 'ybom', 'start': 0.35, 'end': 0.40, 'rate': get_rate()})
    kit.set('b', lambda: {'name': 'ybom', 'start': 0.40, 'end': 0.34, 'rate': get_rate()})
    kit.set('c', lambda: {'name': 'ybom', 'start': 0.25, 'end': 0.30, 'rate': get_rate()})

    kit.seq('moby', [
        'a-b-c---a-b-c--',
    ])
    
    kit.play('moby')


@loop('mobylette', beats=4)
def bass():
    kit = sampler.Kit(sp1)

    return

    def get_rate():
        r = [1/12*11, 1/12*8]
        rate = r[int(rnd.between(0, len(r)))]
        if rnd.one_in(2):
            rate = -rate
        return rate

    kit.set('a', lambda: {'name': 'ybom', 'start': 0.35, 'end': 0.40, 'rate': get_rate()})
    kit.set('b', lambda: {'name': 'ybom', 'start': 0.40, 'end': 0.34, 'rate': get_rate()})
    kit.set('c', lambda: {'name': 'ybom', 'start': 0.25, 'end': 0.30, 'rate': get_rate()})

    kit.seq('moby', [
        'a-------a------',
    ])
    
    kit.play('moby')


system.record('wtf.wav')
    
   
@loop('beats', beats=4)
def beat():
    kit = sampler.Kit(sp2)

    return

    kit.set('k', lambda: {'name': 'bd-606-01'})
    kit.set('o', lambda: {'name': 'oh-606-mod-23', 'amp': 0.2, 'end': 0.3})
    kit.set('c', lambda: {'name': 'ch-606-01', 'amp': 0.3, 'end': 0.3, 'rate': rnd.between(0.99, 1.01), 'pan': rnd.between(-0.2, -0.4)})
    kit.set('C', lambda: {'name': 'crash-909-01', 'rate': -1})

    kit.seq('0x00', [
        'k-------k-------k-------k-------',
        '----o-------o-------o-------o---',
    ])

    kit.seq('0x01', [
        'k-------k-------k-------k-------',
        '----o-------o-------o-------o---',
        '--c--c----c--cc---c---c--c-cc-cc',
    ])

    flavors = ['0x01']

    kit.play(flavors[int(rnd.between(0, len(flavors)))])
