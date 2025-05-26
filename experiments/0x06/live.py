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
    """A simple kit for playing patterns of samples.

        This class allows you to define a set of samples (or "plays") that can be
        triggered by characters, and then create sequences of these characters to
        play patterns.

        Example usage:

        ```python
        sp = sampler.new('my-sample-pack')
    
        kit = Kit(sp)

        kit.set('k', lambda: {'name': 'bd-808'})
        kit.set('s', lambda: {'name': 'sd-808'})

        kit.seq('basic', [
            'k-------k-------',
            '--------s-------',
        ])

        kit.play('basic')
        ```

        This will play a basic kick and snare pattern using the defined samples.
    """
    def __init__(self, sp: sampler.Sampler):
        """Initialize the Kit with a sampler instance.

        Args:
            sp (sampler.Sampler): The sampler instance to use for playing samples.
        """
        self.sp = sp
        self.duration = current_loop().beats
        self.kit = dict()
        self.patterns = dict()

    def set(self, char: str, mkplay: callable) -> None:
        """Set a character to a sample play function.

        Args:
            char (str): The character that will trigger the sample.
            mkplay (callable): A function that returns a dictionary of sample parameters.
        """
        self.kit[char] = mkplay

    def seq(self, flavor: str, sequences: list[str]) -> None:
        """Define a sequence of samples for a given flavor.

        Args:
            flavor (str): The name of the sequence flavor.
            sequences (list[str]): A list of strings, each representing a sequence of characters.
        Raises:
            ValueError: If the sequences are not of the same length.
        """
        steps = {len(x) for x in sequences}
        if len(steps) != 1:
            raise ValueError('DrumKit sequences must be of the same duration')
        self.patterns[flavor] = sequences

    def play(self, flavor: str) -> None:
        """Play a sequence of samples defined by the flavor.

        Args:
                flavor (str): The name of the sequence flavor to play.
        Raises:
                ValueError: If the flavor does not exist in the patterns.
        """
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
