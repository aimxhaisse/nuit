# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

@live()
def setup():
    bpm.set(130)

    ctrls.mk_lfo('x1', 0.25, low=0.1, high=0.6)

    tracks.setup({
        'beats': tracks.mk_sampler(),
    })


sp = sampler.new('elektron-2323')
    

class Kit:
    def __init__(self, sp: sampler.Sampler):
        self.sp = sp
        self.duration = current_loop().beats
        self.kit = dict()
        self.patterns = dict()

    def set(self, char: str, mkplay: callable) -> None:
        self.kit[char] = mkplay

    def seq(self, flavor: str, sequences: list[str]) -> None:
        steps = {len(x) for x in sequences}
        if len(steps) != 1:
            raise ValueError('DrumKit sequences must be of the same duration')
        self.patterns[flavor] = sequences

    def play(self, flavor: str) -> None:
        pattern = self.patterns.get(flavor)
        if not pattern:
            raise ValueError(f"DrumKit has no flavor named {flavor}")

        steps = len(pattern[0])
        dur = self.duration / steps

        for i in range(steps):
            for p in pattern:
                what = self.kit.get(p[i])
                if what:
                    sp.play(**what())
            sleep(dur)



@loop('beats', beats=4)
def beat():
    kit = Kit(sp)

    kit.set('k', lambda: {'name': 'bd-606-01'})
    kit.set('s', lambda: {'name': 'sd-909-sat-c-02'})
    kit.set('o', lambda: {'name': 'oh-606-mod-23', 'amp': 0.2, 'end': 0.3})
    kit.set('c', lambda: {'name': 'ch-606-01', 'amp': 0.3, 'end': 0.3, 'rate': rnd.between(0.99, 1.01), 'pan': rnd.between(-0.2, -0.4)})
    kit.set('C', lambda: {'name': 'crash-909-01', 'rate': -1})
    kit.set('S', lambda: {'name': 'sd-606-mod-c-08'})

    kit.seq('0x00', [
        'k-------k-------k-------k-------',
        '--------s---------------s-------',
        '----o-------o-------o-------o---',
    ])

    kit.seq('0x01', [
        'k-------k-------k-------k-------',
        '--------s---------------s-------',
        '----o-------o-------o-------o---',
        '--c--c----c--cc---c---c--c-cc-cc',
    ])

    kit.seq('0x02', [
        'k-------k-------k-------k-------',
        '--------s---------------s-------',
        '----o-------o-------o-------o---',
        '--c--c----c--cc---c---c--c-cc-cc',
        '----------------C---------------',
    ])

    kit.seq('0x03', [
        'k-------k-------k-------k-------',
        '--------s---------------s-------',
        '----o-------o-------o-------o---',
        '--c--c----c--cc---c---c--c-cc-cc',
        '--------S---------------S---S---',
    ])

    flavors = ['0x00', '0x01', '0x02', '0x03']

    kit.play(flavors[int(rnd.between(0, len(flavors)))])
