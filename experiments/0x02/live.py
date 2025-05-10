# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

@live()
def setup():
    bpm.set(120)

    ctrls.mk_lfo('x1', 0.37, low=0.2, high=0.5)

    tracks.setup({
        'track-1': tracks.mk_sampler(fxs={
            'lpf': fx.mk_lpf(cutoff=ctrl('x1')),
        }),
        'track-2': tracks.mk_sampler(fxs={}),
    })

sp_cells = sampler.new('hexcells')
sp_hazard = sampler.new('hazardous')

@loop('track-1', beats=16)
def beats():
    sp_cells.play(sampler.samples('hexcells')[28].name, rate=-1)
    sp_cells.play(sampler.samples('hexcells')[29].name, rate=1)
    sleep(8)
    sp_cells.play(sampler.samples('hexcells')[37].name, rate=0.5)

@loop('track-2', beats=4)
def more_beats():
    if rnd.one_in(7):
        sp_cells.play(sampler.samples('hexcells')[40].name, rate=1.0)

@loop('track-2', beats=4)
def drums():
    sp_cells.play(sampler.samples('hexcells')[54].name, rate=1.0)
    sleep(2)
    sp_cells.play(sampler.samples('hexcells')[54].name, rate=1.0)
    sleep(2)

@loop('track-2', beats=16)
def hazard_1():
    sp_hazard.play(sampler.samples('hazardous')[8].name, rate=rnd.between(0.9, 1.02), pan=ctrl('x1'))

    # Long sample, worth exploring it instead of just playing it.
    sp_hazard.play(sampler.samples('hazardous')[7].name, rate=rnd.between(0.6, 0.8))
