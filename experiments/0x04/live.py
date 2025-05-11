# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

@live()
def setup():
    bpm.set(120)

    ctrls.mk_lfo('x1', 0.05, low=0.3, high=0.37)
    ctrls.mk_lfo('x2', 0.02, low=-0.2, high=0.1)
    ctrls.mk_lfo('x3', 0.5, low=-0.5, high=-0.2)
    ctrls.mk_lfo('x4', 0.5, low=0.5, high=0.9)

    ctrls.mk_lfo('x5-bass', 8, low=0.1, high=0.8)

    trks = {}

    trks['trk-1'] = tracks.mk_sampler(fxs={
        'rev': fx.mk_reverb(),
        'lpf': fx.mk_lpf(cutoff='x1'),
        'chorus': fx.mk_chorus(depth=0.99),
    }, pan=ctrl('x2'))

    trks['trk-2'] = tracks.mk_sampler(fxs={
        'lpf': fx.mk_lpf(cutoff='x1'),
    })

    trks['trk-3'] = tracks.mk_sampler(fxs={
        'hpf': fx.mk_lpf(cutoff=0.9),
    })

    tracks.setup(trks)

oberheim = sampler.new('oberheim')
hexcells = sampler.new('hexcells')
    
@loop('trk-1', 32)
def cumbersome_bass():
    sp = sampler.samples('oberheim')[50]

    oberheim.play(sp.name, rate=0.75, amp=ctrl('x5-bass'), pan=-0.3)
    oberheim.play(sp.name, rate=-0.76, amp=ctrl('x5-bass'), pan=0.2)

@loop('trk-2', 8)
def low_kicks():
    spk = sampler.samples('hexcells')[7]
    sps = sampler.samples('hexcells')[9]

    hexcells.play(spk.name, amp=0.7)
    sleep(4)
    hexcells.play(sps.name, amp=0.8)
    
@loop('trk-3', 4)
def high_kicks():
    spk = sampler.samples('hexcells')[10]
    
    for i in range(1):
        hexcells.play(spk.name, amp=0.7)
        sleep(2)

@loop('trk-3', 4)
def randoms():

    if rnd.one_in(7):
        sp = sampler.samples('hexcells')[35]
        sleep(rnd.between(0, 3))
        hexcells.play(sp.name, amp=0.2, pan=ctrl('x3'))

    elif rnd.one_in(9):
        sp = sampler.samples('hexcells')[39]
        sleep(rnd.between(0, 2))
        hexcells.play(sp.name, amp=0.2, pan=ctrl('x4'))

    elif rnd.one_in(3):
        sp = sampler.samples('hexcells')[43]
        sleep(rnd.between(0, 2))
        hexcells.play(sp.name, amp=0.2, rate=rnd.between(0.4, 1.0), pan=rnd.between(-1.0, 1.0))
