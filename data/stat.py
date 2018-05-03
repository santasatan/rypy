def statdesc(nda):
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt 
    
    # Text Description
    print('mean:', nda.mean())
    print('max:', nda.max())
    print('min:', nda.min())
    print('StDev:', np.std(nda))
    print('Q1:', np.percentile(nda, 25))
    print('mdeian:', np.median(nda))
    print('Q3:', np.percentile(nda, 75))
    
    # Box plot
    # Median
    dd = plt.boxplot(nda)
    x, y = dd['medians'][0].get_xydata()[1]
    plt.text(x, y, y, horizontalalignment='left', verticalalignment='center')

    # Q1
    x, y = dd['boxes'][0].get_xydata()[0]
    plt.text(x, y, y, horizontalalignment='right', verticalalignment='top')

    # Q3
    x, y = dd['boxes'][0].get_xydata()[3]
    plt.text(x, y, y, horizontalalignment='right', verticalalignment='bottom')

    # Max
    x, y = dd['caps'][1].get_xydata()[1]
    plt.text(x, y, y, horizontalalignment='left', verticalalignment='center')

    # Min
    x, y = dd['caps'][0].get_xydata()[1]
    plt.text(x, y, y, horizontalalignment='left', verticalalignment='center')
    plt.show()
    
    #Histgram
    plt.hist(nda)