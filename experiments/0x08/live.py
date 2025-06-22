# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev


class Kit:
    """A simple kit for playing patterns of samples.

        This class allows you to define a set of samples (or "plays") that can be
        triggered by characters, and then create sequences of these characters to
        play patterns.

        Example usage:

        ```python
        sp = sampler.new('my-sample-pack')
    
        kit = sampler.Kit(sp)

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


@live()
def setup():
    bpm.set(130)

    tracks.setup({
        'beats': tracks.mk_sampler(),
        'beats-high': tracks.mk_sampler(fxs={
            'hpf': fx.mk_hpf(cutoff=0.4, resonance=0.2),
        }),
    })


sp = sampler.new('elektron-2323')

    
# Bass ideas: kit.set('o', lambda: {'name': 'oh-606-mod-03', 'end': 0.2})

@loop('beats', beats=4)
def beat_base():
    kit = Kit(sp)

    kit.set('k', lambda: {'name': 'bd-606-01'})
    kit.set('K', lambda: {'name': 'bd-808-sp-01', 'start': 0.05, 'end': 0.15, 'amp': 0.3})
    kit.set('s', lambda: {'name': 'sd-606-mod-a-04', 'rate': 0.5, 'amp': 0.5})
    kit.set('S', lambda: {'name': 'cy-606-mod-01'})

    kit.seq('0x00', [
        'k-------k-------k-------k-------',
        '---K-K----K---K---K---K----K-K--',
        '--------s---------------s-------',
        '--------S---------------S-------',
    ])

    kit.play('0x00')

    
@loop('beats-high', beats=4)
def beats_percs():
    kit = Kit(sp)

    kit.set('o', lambda: {'name': 'oh-909-01', 'amp': 0.4, 'pan': rnd.between(0.2, 0.4)})
    kit.set('O', lambda: {'name': 'oh-909-02', 'amp': 0.2, 'pan': rnd.between(-0.2, -0.4)})

    kit.seq('0x00', [
        '----o-------o-------o-------o---',
        '----O-------O-------O-------O---',
    ])

    kit.play('0x00')
